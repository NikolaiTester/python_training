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
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(
        name="nameModify",
        middlename="middlenameModify",
        lastname="lastnameModify",
        address="addressModyfy",
        homephone="home",
        mobilephone="mobile",
        workphone="work",
        email="emailModify",
        email2="email2Modify",
        email3="email3Modify",
        secondaryphone="phone2"
    )
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)