from model.contact import Contact
import time
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(name="name",
                    middlename="middlename",
                    lastname="lastname",
                    nickname="nickname",
                    title="title",
                    company="company",
                    address="address",
                    mobile="mobile",
                    workmobile="work",
                    fax="fax",
                    email="email",
                    email2="email2",
                    email3="email3",
                    homepage="homepage",
                    byear="byear",
                    ayear="ayear",
                    address2="address2",
                    phone2="phone2",
                    notes="notes",
                    home="home"
                    ))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    time.sleep(2)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[index:index+1] = []
    assert old_contact == new_contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
