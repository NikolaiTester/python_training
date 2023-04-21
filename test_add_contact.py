# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import ApplicationContact

@pytest.fixture()
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address="address", mobile="mobile", workmobile="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage", byear="byear", ayear="ayear", address2="address2", phone2="phone2", notes="notes", home="home" ))
    app.return_to_home()
    app.logout()
