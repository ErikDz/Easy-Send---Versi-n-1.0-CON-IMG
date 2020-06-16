# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:37:43 2020

@author: erikd
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import re

from selenium.webdriver.common.keys import Keys

import xerox

class EasySend:
    
    def __init__(self, driver):
        global counter
        counter = 0
        self.driver = driver


    def mandar_rapido_teclas(self, mensaje):
        xerox.copy(mensaje)


   
    
    def buscar_contacto(self, contacto):
        self.driver.find_element_by_xpath('//*[@title="Nuevo chat"]').click()
        buscar_chat_tag = self.driver.find_element_by_class_name('_3FRCZ.copyable-text.selectable-text')


        #buscar_chat_tag.send_keys(contacto)
        xerox.copy(contacto)
        buscar_chat_tag.send_keys(Keys.CONTROL,'v')


        time.sleep(0.1)
        try:
            self.driver.find_element_by_xpath('//div[@id="main"]//*[@title="{0}"]'.format(contacto))
        except:
            time.sleep(0.1)
            
        buscar_chat_tag.send_keys(Keys.ENTER)
    
    
    def mandar_mensaje(self, mensaje):
        message_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#Separamos el mensaje si hay un nuevo reglón

        """
        try:
            mensaje = mensaje.split("\n")
        except:
            print("No espacios")

        print(mensaje)


        for i in range(len(mensaje)-1):
            message_box.send_keys(mensaje[i])
            message_box.send_keys(Keys.SHIFT, Keys.ENTER)
        """
        xerox.copy(mensaje)
        message_box.send_keys(Keys.CONTROL,'v')
        message_box.send_keys(Keys.ENTER)

        
        
    def mandar_archivo(self, location):
        #To send attachments
        #click to add

        #Hay que hacer esto de los while para velocidad

        
        if len(self.driver.find_elements_by_class_name("_3nEwM")) > 0: #Checkeamos si ha encontrado el contacto
            raise Exception("No se ha encontrado el contacto") #Si no, raiseamos un error que nos entrará en el try loop del mandar a todo el mundo
 

        while True:
            try:
                clip = self.driver.find_element_by_css_selector("span[data-icon='clip']")
                clip.click()
                break
                print("Salido del clip")
            except:
                pass
        #add file to send by file path
        while True:
            try:
                file = self.driver.find_element_by_css_selector("input[type='file']")
                file.send_keys(location)
                break
                print("Salido del archivo")
            except Exception as ex:
                print(ex)
                pass
        #click to send
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
                break
            except:
                pass

        print("Salido de mandar mandar_archivo")

        
    
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



