from model.contact import Contact
from random import randrange

def test_modify_contact(app):
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
    contact = Contact(
        name="nameModify",
        middlename="middlenameModify",
        lastname="lastnameModify",
        nickname="nicknameModify",
        title="titleModify",
        company="companyModify",
        address="addressModyfy",
        mobile="mobileModify",
        workmobile="workModify",
        fax="faxModify",
        email="emailModify",
        email2="email2Modify",
        email3="email3Modify",
        homepage="homepageModify",
        byear="Mod1",
        ayear="1999",
        address2="address2Modify",
        phone2="phone2Modify",
        notes="notesModify",
        home="homeModify"
    )
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)