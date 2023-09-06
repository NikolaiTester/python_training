from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name",
                    middlename="middlename",
                    lastname="lastname",
                    nickname="nickname",
                    title="title",
                    company="company",
                    address="address",
                    homephone="home",
                    mobilephone="mobile",
                    workphone="work",
                    fax="fax",
                    email="email",
                    email2="email2",
                    email3="email3",
                    homepage="homepage",
                    byear="byear",
                    ayear="ayear",
                    address2="address2",
                    secondaryphone="phone2",
                    notes="notes"
                    ))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    contact.id = str(old_contacts[index].id)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)