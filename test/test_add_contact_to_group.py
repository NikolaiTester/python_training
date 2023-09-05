from model.contact import Contact
from model.group import Group
import random
def test_add_contact_to_group(app, db, orm):
    # проверяем наличие хотя бы одного контакта. Если его нет - создаем
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Nikolai", last_name="Test", address="Санкт-Петербург", mobilephone="7911095563", homephone="89110975565",
                                workphone="89110975567", secondaryphone="89110975568", email="email@email.ru",
                                email2="email2@email.ru", email3="email3@email.ru"))
    # выбираем случайный контакт
  #  contacts = db.get_contact_list()
   # contact = random.choice(contacts)
    # проверяем наличие хотя бы одной группы. Если её нет - создаем
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_del"))
    # выбираем случайную группу
    groups = db.get_group_list()
    group = random.choice(groups)
    # добавляем контакт в группу
    contacts_for_add_in_group = orm.get_contacts_not_in_group(group)
    if contacts_for_add_in_group == []:
        app.contact.add(Contact(first_name="Nikolai", last_name="Test", address="Санкт-Петербург", mobilephone="7911095563",
                                homephone="89110975565",
                                workphone="89110975567", secondaryphone="89110975568", email="email@email.ru",
                                email2="email2@email.ru", email3="email3@email.ru"))
        contact_for_add_in_group = orm.get_contacts_not_in_group(group)[0]
    else:
        contact_for_add_in_group = random.choice(contacts_for_add_in_group)
    app.contact.add_contact_to_group(contact_for_add_in_group, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_add_in_group in contacts_in_group