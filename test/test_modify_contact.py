from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(name="name12", lastname="lastname123", address="address123")
    contact_modify.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_modify)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)