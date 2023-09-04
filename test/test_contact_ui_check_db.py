import re
from random import randrange
from model.contact import Contact


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))

def test_contact_ui_chech_db(app):
    app.contact.open_home_page()
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
def test_info_on_home_page_with_db(app, db):
    app.contact.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(name="name1", middlename="middlename1", lastname="lastname1", workphone='+7905905905', homephone='112124', email2='test@test.test', email3='email3'))
        app.contact.return_to_home_page()
    contact_from_home_page = sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key = Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)

    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].name == contact_from_db[i].name
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_db[i])
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_db[i])

