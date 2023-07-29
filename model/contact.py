from sys import maxsize
class Contact:


    def __init__(self,
                 middlename=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 mobile=None,
                 workmobile=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 byear=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 home=None,
                 name=None,
                 lastname=None,
                 id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.workmobile = workmobile
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.home = home
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.name == other.lastname and self.lastname == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize