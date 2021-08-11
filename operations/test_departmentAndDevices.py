import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import selenium
import pytest

class Test_workplace():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/admin/login")
        self.driver.find_element_by_id('admin_login__input--login').send_keys('admin')
        self.driver.find_element_by_id('admin_login__input--password').send_keys('admin')

        self.driver.find_element_by_id('admin_login__nz-select--authorizationRole').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("nz-option-item[title='Центральный администратор']").click()

        self.driver.find_element_by_id('admin_login__button--submit').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('modal-dialog__button--submit').click()

    def teardown(self):
        self.driver.quit()

    @allure.feature('Open page')
    @allure.story('Открываем страницу "Отделения и устройства"')
    @allure.severity('blocker')
    #@allure.description('*Название тест-кейса*')
    def test_goToDepartamentAndDevices(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('admin_main__div--submit-0').click()
        #finally:
            #if (AssertionError):
                #allure.attach(self.driver.get_screenshot_as_png(), name='FirstScreen',attachment_type=AttachmentType.PNG)
        except selenium.common.exceptions.NoSuchElementException:
            raise pytest.fail("Элемент не найден")


    @allure.feature('Тестируемый функционал - id элементов')
    @allure.story('Щелчок по боковому меню')
    @allure.severity('critical')
    def test_openMenu(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('sidebar__div--show').click()
            assert "main" in self.driver.current_url
            if ("main" in self.driver.current_url):
                with allure.step('Делаем скриншот'):
                    allure.attach(self.driver.get_screenshot_as_png(), name='SecondScreen',attachment_type=AttachmentType.PNG)
        except selenium.common.exceptions.NoSuchElementException:
            raise pytest.fail("Сообщение об ошибке")

class Test_SecondClass():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/admin/login")
        self.driver.find_element_by_id('admin_login__input--login').send_keys('admin')
        self.driver.find_element_by_id('admin_login__input--password').send_keys('admin')

        self.driver.find_element_by_id('admin_login__nz-select--authorizationRole').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("nz-option-item[title='Центральный администратор']").click()

        self.driver.find_element_by_id('admin_login__button--submit').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('modal-dialog__button--submit').click()

    def teardown(self):
        self.driver.quit()

    @allure.feature('Тестируемый функционал - id элементов')
    @allure.story("Переход на страницу 'Справочники' ")
    @allure.description('Проверка id кнопки перехода на страницу Справочники')
    def test_goToGuide(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('admin_main__div--submit-1').click()
        except selenium.common.exceptions.NoSuchElementException:
            raise pytest.fail("Элемент не найден")
