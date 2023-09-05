from sys import maxsize
class Contact:


    def __init__(self,
                 all_emails_from_home_page=None,
                 all_phones_from_home_page=None,
                 first_name=None,
                 middlename=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 byear=None,
                 ayear=None,
                 address2=None,
                 secondaryphone=None,
                 notes=None,
                 last_name=None,
                 id=None):
        self.name = first_name
        self.middlename = middlename
        self.lastname = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (
        self.id, self.name, self.lastname, self.address, self.all_emails_from_home_page,
        self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.name == other.name and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize