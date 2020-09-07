# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:37:43 2020

@author: erikd
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import re
import random

from selenium.webdriver.common.keys import Keys

import xerox

class EasySend:
    
    def __init__(self, driver):
        global counter
        counter = 0
        self.driver = driver


    def random_spaces(self, mensaje):#Esto ponemos un espacio random en algún sitio del mensaje para evitar bloqueo
        nuevo_mensaje = mensaje.split(" ")
        sitio_espacio = random.randint(0, len(nuevo_mensaje))
        nuevo_mensaje.insert(sitio_espacio, " ")

        nuevo_mensaje = " ".join(nuevo_mensaje)

        return nuevo_mensaje



    
    def buscar_contacto(self, contacto):
        self.driver.find_element_by_xpath('//*[@title="Nuevo chat"]').click()
        buscar_chat_tag = self.driver.find_element_by_class_name('_3FRCZ.copyable-text.selectable-text')


        #buscar_chat_tag.send_keys(contacto)
        xerox.copy(contacto)
        buscar_chat_tag.send_keys(Keys.CONTROL,'v')
        time.sleep(0.1)

        #Acepta el contacto y entra en la conversacióm
        buscar_chat_tag.send_keys(Keys.ENTER)

        #Asegurando que ha encontrado el contacto
        text = "No se encontraron resultados para"
        no_encontrado = self.driver.find_elements_by_xpath('//span[contains(text(), "' + text + '")]')

        if len(no_encontrado) != 0:#Si encuentra el texto "No se encontraron resultados para", hace saltar una excepción, que hara
            raise#               self.mandar_a_todo_el_mundo() ir al except (significando saltar contacto)

    def hay_link(self):
        while True:
            try:
                self.driver.find_element_by_xpath('//div[@style="transform: translateY(0px);"]')
                break
            except:
                pass

    def mandar_mensaje(self, mensaje):
        f= open("error_en_mandar_mensaje.txt","w+")
        f.write("We went into mandar_mensaje")

        message_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        xerox.copy(self.random_spaces(mensaje))
        message_box.send_keys(Keys.CONTROL,'v')

        if "://www." in mensaje:#Antes de enviarlo, checkeamos si hay link. Si hay, esperamos al SEO
            self.hay_link()

        message_box.send_keys(Keys.ENTER)



        
        
    def mandar_archivo(self, location):
        #To send attachments
        #click to add

        #Hay que hacer esto de los while para velocidad

        while True:
            try:
                clip = self.driver.find_element_by_css_selector("span[data-icon='clip']")
                clip.click()
                break

            except:
                pass
        #add file to send by file path
        while True:
            try:
                file = self.driver.find_element_by_css_selector("input[type='file']")
                file.send_keys(location)
                break

            except Exception as ex:
                print(ex)
                pass
        #click to send
        while True:
            try:
                self.driver.find_element_by_css_selector("span[data-icon='send']").click()
                break
            except:
                pass
        time.sleep(0.2)

    def esperar_hasta_mandado(self, object):

        while True:

            try:
                todos_ticks = self.driver.find_elements_by_class_name("_1qPwk")
                content = todos_ticks[-1].get_attribute('innerHTML')
                result = (re.search('<span aria-label=" (.*) " data-icon="', content)).group(1)

                if result == "Enviado" or result == "Entregado":
                    break


            except:
                break

        self.mandar_a_todo_el_mundo(self.telefonos, self.mensaje_entero, object)


    def mandar_a_todo_el_mundo(self, telefonos, mensaje_entero, object):
        global counter

        self.telefonos = telefonos
        self.mensaje_entero = mensaje_entero
        

        object.progressBar.setProperty("value", counter)
        _translate = QtCore.QCoreApplication.translate
        object.label_23.setText(_translate("Dialog", "Enviado a {0} de {1} contactos...").format(counter, len(telefonos)))

        try:

            self.driver.set_window_size(480,200)
            self.buscar_contacto(str(self.telefonos[counter]))
            for element in self.mensaje_entero:#Aqui, como el mensaje_entero es una lista de [nombre de funcion, contenido], lo runeamos asi
                element[0](*element[1])

            counter += 1

            self.esperar_hasta_mandado(object)

        except Exception as e:#Digamos que no lo encontro
            f= open("error_log.txt","w+")
            f.write(str(e))
            f.close()

            if counter < len(self.telefonos):
                counter +=1
                try:
                    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span').click()
                except:
                    self.driver.set_window_size(480,200)
                
                self.esperar_hasta_mandado(object)

            else:
                object.label_23.setText(_translate("Dialog", "Finalizado: {0} mensajes enviados").format(counter))






