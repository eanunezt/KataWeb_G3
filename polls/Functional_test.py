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

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('D:\Imagenes\developer.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan660')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        self.browser.get("http://localhost:8000")
        login = self.browser.find_element_by_id('id_login')
        login.click()
        username = self.browser.find_element_by_id('id_login_username')
        username.send_keys('juan648')
        password = self.browser.find_element_by_id('id_login_password')
        password.send_keys('clave123')
        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)
        logout = self.browser.find_element_by_id('id_logout')

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

        # Editar
        self.browser.implicitly_wait(5)
        editar = self.browser.find_element_by_id('id_editar')
        sleep(4)
        editar.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Jose Andres')

        # Grabar
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        strong = self.browser.find_element(By.XPATH, '//strong[text()="SUCCESS: "]')
        self.assertIn('SUCCESS:', str(strong.text))

    def test_comentar(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        link = self.browser.find_element_by_id('trabajador8')
        link.click()

        # Correo
        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('correoIndep@uniandes.edu.co')

        # Comentario
        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Comentario a independiente')

        botonComentar = self.browser.find_element_by_id('id_comentario')
        botonComentar.click()

        h4 = self.browser.find_element(By.XPATH, '//h4[text()="correoIndep@uniandes.edu.co"]')
        self.assertIn('correoIndep@uniandes.edu.co', str(h4.text))
