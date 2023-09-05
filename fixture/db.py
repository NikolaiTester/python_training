import pymysql.cursors
from model.group import Group
from model.contact import Contact
from model.contact_in_group import ContactInGroup

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id, name, header, footer)= row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2 FROM addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address, email=email, email2=email2, email3=email3, homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                    all_emails_from_home_page=(email+email2+email3), all_phones_from_home_page=(home+mobile+work+phone2)))
        finally:
            cursor.close()
        return list

    def get_contact_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, group_id FROM address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(ContactInGroup(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
            return list
    def get_contact_in_group(self, group):
        self.get_contact_in_group_list(group)

    def get_contact_in_group(self, group):
        self.get_contact_in_group_list(group)

    def destroy(self):
        self.connection.close()