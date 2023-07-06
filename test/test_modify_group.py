from model.group import Group

def test_modify_group(app):
    app.group.modify_first_group(Group(name="testModify", header="headerModify", footer="footerModify"))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="testModify123"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="headerModify123"))