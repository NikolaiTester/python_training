from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.modify_first_group(Group(name="testModify", header="headerModify", footer="footerModify"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.modify_first_group(Group(name="testModify123"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.modify_first_group(Group(header="headerModify123"))