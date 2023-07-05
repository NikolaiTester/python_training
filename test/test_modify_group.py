from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="testModify", header="headerModify", footer="footerModify"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="testModify123"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="headerModify123"))
    app.session.logout()