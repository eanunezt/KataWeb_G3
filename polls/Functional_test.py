__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("D:\\PythonWorkspace\\KataWeb_G3\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()



    def test_comentar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('trabajador')
        link.click()

        #Correo
        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('correoIndep@uniandes.edu.co')

        #Comentario
        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Este es un comentario')

        botonComentar = self.browser.find_element_by_id('comentar')
        botonComentar.click()

        h4 = self.browser.find_element(By.XPATH, '//h4[text()="correoIndep@uniandes.edu.co "]')
        self.assertIn('correoIndep@uniandes.edu.co', str(h4.text))
