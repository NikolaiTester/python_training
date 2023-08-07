# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(name=firstname, lastname=lastname, middlename=middlename)
    for lastname in ["", random_strint("lastname", 10)]
    for firstname in ["", random_strint("name", 10)]
    for middlename in ["", random_strint("middlename", 10)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

