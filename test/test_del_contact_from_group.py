from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    # Проверяем есть ли хотя бы одна группа
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    groups = db.get_group_list()
    group = random.choice(groups)
    # Проверяем есть ли хотя бы один контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Nikolai", last_name="Test", address="Санкт-Петербург", mobilephone="7911095563", homephone="89110975565",
            workphone="89110975567", secondaryphone="89110975568", email="email@email.ru",
            email2="email2@email.ru", email3="email3@email.ru"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    # Проверяем есть ли контакт в группе
    if len(db.get_contact_in_group_list()) == 0:
        app.contact.add_contact_to_group(contact)
    # Сам тест
    contacts_with_groups = db.get_contact_in_group_list()
    contact_with_group = random.choice(contacts_with_groups)
    app.contact.delete_contact_from_group(contact_with_group)

    contacts_in_group = db.get_contact_in_group_list()
    assert contact_with_group not in contacts_in_group