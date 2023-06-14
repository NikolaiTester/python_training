from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="testModify", header="headerModify", footer="footerModify"))
    app.session.logout()