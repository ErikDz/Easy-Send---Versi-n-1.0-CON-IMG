# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:37:43 2020

@author: erikd
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import re

from selenium.webdriver.common.keys import Keys

class EasySend:
    
    def __init__(self, driver):
        global counter
        counter = 0
        self.driver = driver

   
    
    def buscar_contacto(self, contacto):
        self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]').click()
        buscar_chat_tag = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
        buscar_chat_tag.send_keys(contacto)
        time.sleep(1)
        buscar_chat_tag.send_keys(Keys.ENTER)
    
    
    def mandar_mensaje(self, mensaje):
        message_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#Separamos el mensaje si hay un nuevo reglón

        try:
            mensaje = mensaje.split("\n")
        except:
            print("No espacios")

        print(mensaje)

        for i in range(len(mensaje)-1):
            message_box.send_keys(mensaje[i])
            message_box.send_keys(Keys.SHIFT, Keys.ENTER)



        message_box.send_keys(mensaje[-1])
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)
        
        
    def mandar_archivo(self, location):
        #To send attachments
        #click to add
        self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
        #add file to send by file path
        self.driver.find_element_by_css_selector("input[type='file']").send_keys(location)
        #click to send
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
        time.sleep(1)
        
    
    def esperar_hasta_mandado(self, object):

        while True:
            print("Im okay")
            try:
                todos_ticks = self.driver.find_elements_by_class_name("_1qPwk")
                content = todos_ticks[-1].get_attribute('innerHTML')
                result = (re.search('<span aria-label=" (.*) " data-icon="', content)).group(1)

                if result == "Enviado" or result == "Entregado":
                    print("Enviado Jefe")
                    
                    break

                else:
                    print("Ahun no ha sido enviado")

            except:
                break

        self.mandar_a_todo_el_mundo(self.nombres, self.mensaje_entero, object)


    def mandar_a_todo_el_mundo(self, nombres, mensaje_entero, object):
        global counter

        self.nombres = nombres
        self.mensaje_entero = mensaje_entero
        

        object.progressBar.setProperty("value", counter)
        _translate = QtCore.QCoreApplication.translate
        object.label_23.setText(_translate("Dialog", "Enviado a {0} de {1} contactos...").format(counter, len(nombres)))

        try:

    
            self.buscar_contacto(self.nombres[counter])
            for element in self.mensaje_entero:#Aqui, como el mensaje_entero es una lista de [nombre de funcion, contenido], lo runeamos asi
                element[0](*element[1])

            counter += 1

            self.esperar_hasta_mandado(object)

        except:#Digamos que no lo encontro

            if counter < len(self.nombres):
                counter +=1
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span').click()
                self.esperar_hasta_mandado(object)
            else:

                print("Finiquitado")



