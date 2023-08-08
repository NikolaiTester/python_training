from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

# Класс-менеджер, который инициализирует всех помощников
class Application:

# создание фикстур, инициализация драйвера
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.implicitly_wait(1)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(1)
        elif browser == "ie":
            self.wd = webdriver.Ie()
            self.wd.implicitly_wait(1)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
# конструирование помощников, передаем ссылку на саму фикстуру
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.open_home_page()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

# Метод разрушает фикстуру, останавливает браузер
    def destroy(self):
        self.wd.quit()

    def return_to_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()
        wd.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False