# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="name",
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

def test_add_empty_contact(app):
    app.contact.create(Contact(name="",
                               middlename="",
                               lastname="",
                               nickname="",
                               title="",
                               company="",
                               address="",
                               mobile="",
                               workmobile="",
                               fax="",
                               email="",
                               email2="",
                               email3="",
                               homepage="",
                               byear="",
                               ayear="",
                               address2="",
                               phone2="",
                               notes="",
                               home=""
                               ))