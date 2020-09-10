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

class EasySend(QtCore.QObject):

    signal_update_progress = QtCore.pyqtSignal(int, int)
    
    def __init__(self, driver):
        super(EasySend, self).__init__()
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
        print("mandar_archivo ejecutrado")
        #To send attachments
        #click to add

        #Hay que hacer esto de los while para velocidad

        while True:
            try:#Lo que hace este primer loop es asegurar que esta cerrado el clip para que no se trave
                driver.find_element_by_xpath('//span[@data-testid="attach-document-old"]')
                clip = driver.find_element_by_css_selector("span[data-icon='clip']")
                clip.click()
                time.sleep(0.2)
            except:
                break

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

    def mandar_imagen_y_texto(self, location, mensaje):
        print("mandar_imagen y texto ejecutrado", mensaje)
        #To send attachments
        #click to add
        xerox.copy(self.random_spaces(mensaje))
        #Hay que hacer esto de los while para velocidad
        while True:

            try:#Lo que hace este primer loop es asegurar que esta cerrado el clip para que no se trave
                driver.find_element_by_xpath('//span[@data-testid="attach-document-old"]')
                clip = driver.find_element_by_css_selector("span[data-icon='clip']")
                clip.click()
                time.sleep(0.2)
            except:
                break

        while True:
            try:
                clip = self.driver.find_element_by_css_selector("span[data-icon='clip']")
                clip.click()
                break

            except Exception as e:
                print(e)
                pass


        #add file to send by file path
        while True:
            try:
                file = self.driver.find_element_by_css_selector("input[type='file']")
                file.send_keys(location)
                break

            except Exception as e:
                print(e)
                pass

        #para mandar el mensaje junto a la foto
        while True:
            try:    
                image_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
                xerox.copy(self.random_spaces(mensaje))
                image_text.send_keys(Keys.CONTROL,'v')
                break

            except Exception as e:
                print(e)
                pass

        time.sleep(0.3)

        #Cierra fotos extra
        while True:
            try:
                fotos = self.driver.find_elements_by_xpath("//span[@data-testid='x-alt' and @data-icon='x-alt']")
                print("fotos-detectadas:",len(fotos))
                if len(fotos) > 2:
                    for foto in fotos[1:-1]:
                        foto.click()
                break
                
            except Exception as e:
                pass


        #click to send
        while True:
            try:
                send = self.driver.find_element_by_css_selector("span[data-icon='send']")
                send.click()
                break
            except:
                pass

        time.sleep(0.1)

    def esperar_hasta_mandado(self):

        while True:
            if len(self.driver.find_elements_by_xpath("//span[@data-testid='msg-time']")) == 0:
                break


    def ejecutar_funciones(self, telefono):
        self.driver.set_window_size(480,200)
        element_to_skip = 99999
        for counter_enum, element in enumerate(self.mensaje_entero):#Aqui, como el mensaje_entero es una lista de [nombre de funcion, contenido], lo runeamos asi
            
            #De esta manera comprobamos si quiere mandar un archivo y LUEGO un mensaje y si ese archivo es una imagen     
            try:
                if counter_enum == element_to_skip:
                    print("Paso: ", counter_enum)
                    continue

                elif element[0].__name__ == "mandar_archivo" and self.mensaje_entero[counter_enum + 1][0].__name__ == "mandar_mensaje":
                    if (element[1][0]).endswith("png") or (element[1][0]).endswith("jpg"):
                        element_to_skip = counter_enum+1
                        self.mandar_imagen_y_texto(element[1][0], *self.mensaje_entero[counter_enum + 1][1])
                        self.buscar_contacto(str(telefono))#Buscamos contacto otra vez para librarnos de bug

                else:
                    element[0](*element[1]) #Ejecuta la función normal
                    print("Ejecuto funcion normal")
            except:

                if counter_enum == element_to_skip:
                    continue
                else:
                    element[0](*element[1])


    def mandar_a_todo_el_mundo(self, telefonos, mensaje_entero, object):
        

        counter = 0
        self.telefonos = telefonos
        self.mensaje_entero = mensaje_entero

        for telefono in telefonos:
            self.signal_update_progress.emit(counter, len(telefonos))
            try:
                self.buscar_contacto(str(telefono))
                self.ejecutar_funciones(telefono)
                self.esperar_hasta_mandado()
                counter += 1
                print("")

            except Exception as e:#Digamos que no lo encontro
                print(e)
                if counter < len(self.telefonos):
                    counter +=1
                    try:
                        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span').click()
                    except:
                        #self.driver.set_window_size(480,200)*
                        self.driver.set_window_size(480,200)
                    
                    self.esperar_hasta_mandado()

                else:
                    object.label_23.setText(_translate("Dialog", "Finalizado: {0} mensajes enviados").format(counter))






