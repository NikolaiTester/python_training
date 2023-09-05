from model.contact import Contact
import re
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def completion(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.get(self.app.base_url)
        wd.find_element_by_link_text("add new").click()
        self.completion(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def select_contact_by_index(self, index ):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.completion(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit delition
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # open contacts page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_xpath("//img[@alt='Addressbook']").click()
        xpath = f'//a[@href="edit.php?id={id}"]'
        wd.find_element_by_xpath(xpath).click()
        self.completion(contact)
        # save changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    @staticmethod
    def clear(s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: ContactHelper.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.secondary_phone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

    def merge_emails_from_db(self, contacts):
        merged_users_email_list = []
        for item in contacts:
            merged_users_email_list.append(self.merge_emails(item))
        return merged_users_email_list

    def merge_phones_from_db(self, contacts):
        merged_contacts_phone_list = []
        for item in contacts:
            merged_contacts_phone_list.append(self.merge_phones(item))
        return merged_contacts_phone_list

    def add_contact_to_group(self, contact, group):
        self.app.navigation.return_to_home_page()
        self.select_contact_by_id(contact.id)
        self.select_group_to_add(group.id)
        self.submit_contact_to_group()

    def select_group_to_add(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        # Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_name)
        xpath = f"//select[@name='to_group']/option[@value='{group_id}']"
        wd.find_element_by_xpath(xpath).click()

    def submit_contact_to_group(self):
        wd = self.app.wd
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, contact_with_group):
        self.app.navigation.return_to_home_page()
        self.select_group_with_contact(contact_with_group.group_id)
        self.select_contact_by_id(contact_with_group.id)
        self.submit_delete_contact_to_group()

    def select_group_with_contact(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        xpath = f"//select[@name='group']/option[@value='{group_id}']"
        wd.find_element_by_xpath(xpath).click()

    def submit_delete_contact_to_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()








