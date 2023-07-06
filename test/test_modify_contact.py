from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(name="nameModify", middlename="middlenameModify", lastname="lastnameModify", nickname="nicknameModify", title="titleModify", company="companyModify", address="addressModyfy", mobile="mobileModify", workmobile="workModify", fax="faxModify", email="emailModify", email2="email2Modify", email3="email3Modify", homepage="homepageModify", byear="Mod1", ayear="1999", address2="address2Modify", phone2="phone2Modify", notes="notesModify", home="homeModify"))