# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
                               name="name",
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
                               )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

