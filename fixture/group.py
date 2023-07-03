

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def completion(self, group): # метод заполнения полей
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        self.completion(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.get("http://localhost/addressbook/group.php")
        # select first group
        wd.find_element_by_name("selected[]").click()
        # клик на кнопку редактировать
        wd.find_element_by_name("edit").click()
        # редактирование группы
        self.completion(group)
        # сохранить изменения
        wd.find_element_by_name("update").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.get("http://localhost/addressbook/group.php")
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delition
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()