__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("D:\\PythonWorkspace\\KataWeb_G3\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_editar(self):

        self.browser.get('http://localhost:8000')

        # login usuario
        link = self.browser.find_element_by_id('id_login')
        link.click()
        username = self.browser.find_element_by_id('id_login_username')
        username.send_keys('juan648')
        password = self.browser.find_element_by_id('id_login_password')
        password.send_keys('clave123')
        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)
        logout = self.browser.find_element_by_id('id_logout')

        #Editar
        self.browser.implicitly_wait(5)
        editar = self.browser.find_element_by_id('id_editar')
        sleep(4)
        editar.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Jose Andres')

        #Grabar
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        strong = self.browser.find_element(By.XPATH, '//strong[text()="SUCCESS: "]')
        self.assertIn('SUCCESS:', str(strong.text))
