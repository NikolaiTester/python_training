from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Testgroup1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_modify = Group(name="test123")
    group_modify.id = group.id
    app.group.modify_group_by_id(group.id, group_modify)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_modify)
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
