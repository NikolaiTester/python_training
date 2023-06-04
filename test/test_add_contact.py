# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address="address", mobile="mobile", workmobile="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage", byear="byear", ayear="ayear", address2="address2", phone2="phone2", notes="notes", home="home"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="", middlename="", lastname="", nickname="", title="", company="", address="", mobile="", workmobile="", fax="", email="", email2="", email3="", homepage="", byear="", ayear="", address2="", phone2="", notes="", home=""))
    app.session.logout()