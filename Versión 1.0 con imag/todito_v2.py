
from PyQt5 import QtCore, QtGui, QtWidgets
from convertir_numeros import Leer_xlsx
from convert_to_vcf import hacer_vcard
from funciones import EasySend
import selenium.webdriver 
import time
import threading
from os import getcwd
from send_email import send_email
from math import ceil


from GUI.log_in import log_in
from GUI.seleccionar_archivo import seleccionar_archivo
from GUI.seleccionar_columnas import seleccionar_columnas  
from GUI.introducieno_email import introducieno_email   
from GUI.Diciendo_Que_Aada import Diciendo_Que_Aada
from GUI.waiting_QR import waiting_QR
from GUI.componer_mensaje import componer_mensaje
from GUI.previsualizacion import previsualizacion
from GUI.enviando_progreso import enviando_progreso

class Ui_Dialog(object):
    def __init__(self):
        global columnas, mensaje_entero,contenidos_de_scroll, stop_thread, counter, lista_solo_para_remove
        mensaje_entero = []
        contenidos_de_scroll = []
        lista_solo_para_remove = []
        columnas = ""
        stop_thread = False

        #y = threading.Thread(target=self.constantemente_ajustar)
        #y.start()
        
        counter = 0




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 718)
        Dialog.setStyleSheet("background:rgb(255, 255, 255)")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget.setObjectName("stackedWidget")

        log_in(self)

        seleccionar_archivo(self)

        seleccionar_columnas(self)

        introducieno_email(self)

        Diciendo_Que_Aada(self)

        waiting_QR(self)

        componer_mensaje(self)

        previsualizacion(self)

        enviando_progreso(self)


        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Contraseña:"))
        self.pushButton_Olvidado_contrasena.setText(_translate("Dialog", "Has olvidado tu contraseña?"))
        self.pushButton_LOGIN.setText(_translate("Dialog", "LOG IN"))
        self.label_2.setText(_translate("Dialog", "Usuario:"))
        self.label.setText(_translate("Dialog", "EasySend™"))
        self.label_4.setText(_translate("Dialog", "Selecciona el archivo en el que se encuentran \n"
"los datos de las personas a las que quieres llegar.  "))
        self.pushButton_ConfirmarContinuar_buscar_archivo.setText(_translate("Dialog", "Confirmar y continuar"))
        self.label_que_has_seleccionado.setText(_translate("Dialog", "Has seleccionado:"))
        #self.label_Error.setText(_translate("Dialog", "Error"))
        self.pushButton_buscar_archivo_contactos.setText(_translate("Dialog", "Buscar archivo"))
        self.label_10.setText(_translate("Dialog", "Especifique qué campo contiene los nombres de los destinatarios:\n"
"\n"
"\n"
""))

        self.label_11.setText(_translate("Dialog", "Especifique qué campo contiene los números de teléfono:\n"
"\n"
"\n"
""))

        self.label_encontrado_siguientes_campos.setText(_translate("Dialog", "Se han encontrado los siguientes campos en el archivo contactos.xlsx: \n"
""))
        self.pushButton_confirmarContinuar_campos.setText(_translate("Dialog", "Confirmar y continuar"))


        self.pushButton_confirmarContinuar_ELEMAIL.setText(_translate("Dialog", "Confirmar y continuar"))
        self.lineEdit_entrar_email.setPlaceholderText(_translate("Dialog", "ejemplo@gmail.com"))
        self.label_6.setText(_translate("Dialog", "De esta forma podremos enviarle los contactos al móvil\n"
"para que los añada"))
        self.label_5.setText(_translate("Dialog", "Qué email tiene puesto en su móvil?"))

        self.pushButton_Correo_No_recibido.setText(_translate("Dialog", "<-- No he recibido el correo"))
        self.pushButton_confirmarContinuar_correo.setText(_translate("Dialog", "Confirmar y continuar"))
        self.label_12.setText(_translate("Dialog", "En su dispositivo móvil:"))
        self.label_9.setText(_translate("Dialog", "Ha recibido un email en"))

        self.label_14.setText(_translate("Dialog", "con los contactos"))

        self.pushButton_ConfirmarMensajeComponer.setText(_translate("Dialog", "Confirmar y continuar"))
        self.label_13.setText(_translate("Dialog", "Componga el mensaje que quiere lanzar"))
        self.label_20.setText(_translate("Dialog", "Puedes añadir todos los mensajes y archivos \n"
"que quieras."))
        self.plainTextEdit_hacer_mensaje.setPlaceholderText(_translate("Dialog", "Escriba aquí el mensaje para agregar"))
        self.pushButton_AgregarMensaje.setText(_translate("Dialog", "Agregar mensaje"))
        self.pushButton_AdjuntarUnArchivo.setText(_translate("Dialog", "Adjuntar un archivo"))
        self.label_19.setText(_translate("Dialog", "Así es como se verá:"))
        self.label_21.setText(_translate("Dialog", "Clickea en cualquier mensaje para editarlo"))
        self.label_22.setText(_translate("Dialog", "Así es como se verá:"))
        self.pushButton_ReHacer.setText(_translate("Dialog", "<--   Rehacer"))
        self.pushButton_ENVIAR.setText(_translate("Dialog", "Enviar a (64) contactos"))

        self.label_23.setText(_translate("Dialog", "Enviado a 6 de 64 contactos..."))
        self.label_25.setText(_translate("Dialog", "Deje el móvil cerca del ordenador y no cierre la pestaña del navegador"))


    def log_in_ha_clickeado(self):
        user = "admin"
        password = ""
        if self.lineEdit_Entrar_Usuario.text() == user and self.lineEdit_Contrasena.text() == password: #Se comprobará con server
            print("Login succesful")
            self.stackedWidget.setCurrentIndex(1)#Cambiamos a segunda página
            self.pushButton_ConfirmarContinuar_buscar_archivo.hide()


        """
        _translate = QtCore.QCoreApplication.translate
        self.label_ErrorLogin.setText(_translate("Dialog", "Usuario o contraseña incorrecto"))


        """
            
    def is_clicked_seleccionar_archivo(self):#Aqui pilla el file location y lo pone global
        global filename,leer_xlsx, columnas
        self.pushButton_ConfirmarContinuar_buscar_archivo.hide()
        _translate = QtCore.QCoreApplication.translate#AÑADIR VERIFICAR QUE SEA XLSX
        
        print("todo correcto")
        filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Seleccionar archivo')
        if filename:
            filename = filename[0]


            filename_extension = filename.split(".")[-1]#Pilla la extension de archivo
            if filename_extension != "xlsx":#Si no es xlsx da error
                self.label_que_has_seleccionado.setText(_translate("Dialog","Archivo seleccionado: {0}").format(filename))
                self.label_Error.setText(_translate("Dialog", "Error: Archivo no es .xlsx"))
            else:
                self.label_Error.setText(_translate("Dialog", ""))
                self.pushButton_ConfirmarContinuar_buscar_archivo.show()

                self.label_que_has_seleccionado.setText(_translate("Dialog","Archivo seleccionado: {0}").format(filename))
                
                leer_xlsx = Leer_xlsx(filename)
                
                columnas = leer_xlsx.dar_columnas()#

            
            
    def is_clicked_confirmar_archivo(self):
        
        self.stackedWidget.setCurrentIndex(2)
        self.agregar_titulo_columna()

    def is_clicked_confirmar_columnas(self):
        global columnas, leer_xlsx, filename, nombres, telefonos
        
        nombres_nombre = self.comboBox_nombres.currentText()
        telefono_nombre = self.comboBox_telefonos.currentText()
        
        print(telefono_nombre,nombres_nombre)
        nombres, telefonos = leer_xlsx.ajustar_nombres(nombres_nombre, telefono_nombre, filename)
        
        print("\n\n",nombres, telefonos)

        
        hacer_vcard(nombres, telefonos)
        
        self.stackedWidget.setCurrentIndex(3)

    def is_clicked_confirmar_email(self):
        email = self.lineEdit_entrar_email.text()
        self.stackedWidget.setCurrentIndex(4)
        filename =  getcwd() + "\\test_11.vcf"

        _translate = QtCore.QCoreApplication.translate
        self.label_donde_recibido_email.setText(_translate("Dialog", email))

        thread_mandar_email = threading.Thread(daemon=True, target=send_email , args=("pitypython3@gmail.com", "AltisLife", email, "Abra este archivo en su móvil", filename))
        thread_mandar_email.start()
        #send_email("pitypython3@gmail.com", "AltisLife", email, "Abra este archivo en su móvil", filename)#CAMBIAR EMAIL Y PONER BIEN FILENAME
        
        
    def is_clicked_confirmar_agregado_contactos(self):
        global y, contenidos_de_scroll, stop_thread

        self.stackedWidget.setCurrentIndex(5)
        x = threading.Thread(daemon=True, target=self.abrimos_whatsapp_y_esperamos)#Usamos threading para que no se nos crashee el programa
        x.start()
        #x.join()

        y = threading.Thread(daemon=True, target=self.constantemente_ajustar)

        y.start()


    def is_clicked_correo_no_recibido(self):
        self.stackedWidget.setCurrentIndex(3)

        
    def is_clicked_agregar_mensaje(self):
            self.agregar_texto(self.plainTextEdit_hacer_mensaje.toPlainText())

        
    def is_clicked_agregar_imagen(self):
        directorio = QtWidgets.QFileDialog.getOpenFileName(None, 'Seleccionar archivo')
        directorio = directorio[0]
        print("\n\n\n",directorio,"\n\n\n")
        self.agregar_imagen(directorio)


    def is_clicked_finalizar_componer(self):
        global nombres, EasySend, mensaje_entero, y, stop_thread

        #stop_thread = True
        self.poner_todo_bien()
        self.stackedWidget.setCurrentIndex(7)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton_ENVIAR.setText(_translate("Dialog", "Enviar a ({0}) contactos").format(len(nombres)))


        self.scrollArea_Previsualizar = self.scrollArea
        self.pushButton_ConfirmarMensajeComponer.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";\n"
"margin-bottom:75px;"
"")
        self.scrollArea_Previsualizar.setMinimumSize(QtCore.QSize(500, 0))
        self.horizontalLayout_11.insertWidget(1,self.scrollArea_Previsualizar)



    def is_clicked_enviar(self):
        global stop_thread, nombres
        self.stackedWidget.setCurrentIndex(8)
        self.enviar_a_contacto()

        

        stop_thread = True

    def is_clicked_re_hacer(self):
        global y, lista_solo_para_remove, contenidos_de_scroll, mensaje_entero

        self.stackedWidget.setCurrentIndex(6)

        self.verticalLayout.insertWidget(1,self.scrollArea)#Insertamos de nuevo scrollArea(Ya que se ha movido)



        for element in lista_solo_para_remove: #Quitamos todos los widgets dentro del ScrollArea
            try:
                element.deleteLater()
                element = None
            except:
                pass

        contenidos_de_scroll = [] #Limpiamos las listas que usabamos para guardar los contenidos del scrollArea
        mensaje_entero = []










    #-------------------------------------------------------------------------------------------------    

    

    def agregar_titulo_columna(self):#COGEN EL VALOR DEL NUMERO DE COLUMNAS
        global columnas
        
            
        for columna in columnas:
            
            self.label_campo1 = QtWidgets.QLabel(self.Seleccionar_Columnas)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_campo1.sizePolicy().hasHeightForWidth())
            self.label_campo1.setSizePolicy(sizePolicy)
            self.label_campo1.setStyleSheet("font-size: 20px;\n"
    "color: #707070;\n"
    "font-family: \"Segoe UI\";"
    "margin-left: 30px;\n"
    "font-weight: 450;")
            self.label_campo1.setObjectName("label_campo_"+columna)
            self.verticalLayout_3.addWidget(self.label_campo1)

            _translate = QtCore.QCoreApplication.translate
            self.label_campo1.setText(_translate("Dialog", "-  "+columna))

            self.comboBox_nombres.addItem(columna)
            self.comboBox_telefonos.addItem(columna)



        
    def abrimos_whatsapp_y_esperamos(self):
        global driver, EasySend
        #self.stackedWidget.setCurrentIndex(6)        
        driver = selenium.webdriver.Chrome()
        driver.get("https://web.whatsapp.com/")
        
        EasySend = EasySend(driver)
        time.sleep(6)
    
        #Aqui, buscamos constantemente el código QR. Si está, significa q no se ha logueado
        while True:
            
            try:
                driver.find_element_by_class_name("_1p68X")
                print("encontrado")

            except:
                
                break

        #time.sleep(1)

        
        self.stackedWidget.setCurrentIndex(6)

        driver.minimize_window()
        
        
    def agregar_texto(self, texto):

        global mensaje_entero, contenidos_de_scroll, lista_solo_para_remove


        funcion = EasySend.mandar_mensaje
        mensaje_entero.append([funcion,(texto,)])
        
        self.Ejemplo_Texto = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ejemplo_Texto.sizePolicy().hasHeightForWidth())
        self.Ejemplo_Texto.setSizePolicy(sizePolicy)

        if len(texto) >= 16:
            print(len(texto))
            print("alto:", ceil(len(texto)/40))#Lo que hace ceil es redondear pa arriba
            print("Pixeles:", ((ceil(len(texto)/40)   )*23)+20   )#aqui hay un error, mult x2 cuando sigue siendo 1
            print("")
            self.Ejemplo_Texto.setMinimumSize(QtCore.QSize(360, ((ceil(len(texto)/40)   )*23)+20   ))#Redondeamos pa arriba, mult por 30px (una linea) y añadimos 20px x primera
            self.Ejemplo_Texto.setMaximumSize(QtCore.QSize(360, ((ceil(len(texto)/40)   )*23)+20   ))
        else:
            self.Ejemplo_Texto.setMaximumSize(QtCore.QSize((len(texto)*20), 60))
            self.Ejemplo_Texto.setMinimumSize(QtCore.QSize((len(texto)*20), 60))

        contenidos_de_scroll.append(self.Ejemplo_Texto)#Añadimos el widget a la lista contenidos_de_scroll
        lista_solo_para_remove.append(self.Ejemplo_Texto)



        self.Ejemplo_Texto.setStyleSheet("background: #e1ffc7;\n"
"border-radius: 10px;\n"
"border: 4px solid #e1ffc7;\n"
"float: right;\n"
"top: 0;\n"
"\n"
"margin-bottom: 5px;\n"
"font-size: 16px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:\"Segoe UI\";\n"
"font-weight:1000px;\n"
"")
        self.Ejemplo_Texto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Ejemplo_Texto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Ejemplo_Texto.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Ejemplo_Texto.setTabChangesFocus(False)
        self.Ejemplo_Texto.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.Ejemplo_Texto.setTabStopWidth(80)
        self.verticalLayout_7.addWidget(self.Ejemplo_Texto)
        
        
        _translate = QtCore.QCoreApplication.translate
        self.Ejemplo_Texto.setPlainText(_translate("Dialog", texto))


    def constantemente_ajustar(self):
        global contenidos_de_scroll, stop_thread #Globaliza una lista la cual contiene los widgets
        while stop_thread == False:
            time.sleep(3)
            for widget in contenidos_de_scroll:
                try:
                    texto = widget.toPlainText()#Comprueba el texto en cada widget y re-ajusta como antes
                    if len(texto) >= 16:
                        widget.setMinimumSize(QtCore.QSize(360, ((ceil(len(texto)/40)   )*23)+20   ))#Redondeamos pa arriba, mult por 30px (una linea) y añadimos 20px x primera
                        time.sleep(.5)
                        widget.setMaximumSize(QtCore.QSize(360, ((ceil(len(texto)/40)   )*23)+20   ))
                        time.sleep(.5)
                    else:
                        widget.setMaximumSize(QtCore.QSize((len(texto)*20), 60))
                        time.sleep(.5)
                        widget.setMinimumSize(QtCore.QSize((len(texto)*20), 60))
                        time.sleep(.5)
                except Exception as e:
                    print(e)
                    pass
                time.sleep(1)
        


            time.sleep(4)#Se pone un sleep de 5 segundos para que no se crashee
            



        
    def agregar_imagen(self, directorio):
        global mensaje_entero, lista_solo_para_remove

        funcion = EasySend.mandar_archivo
        mensaje_entero.append([funcion,(directorio,)])
        

        self.Ejemplo_Imagen = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ejemplo_Imagen.sizePolicy().hasHeightForWidth())
        self.Ejemplo_Imagen.setSizePolicy(sizePolicy)
        self.Ejemplo_Imagen.setStyleSheet("background: #e1ffc7;\n"
"border-radius: 10px;\n"
"border: 4px solid #e1ffc7;\n"
"float: right;\n"
"top: 0;\n"
"\n"
"margin-bottom: 5px;\n"
"font-size: 16px;\n"
"color: rgb(0, 0, 0);\n"
"font-family: \"Roboto\", sans-serif;\n"
"font-weight:800px;\n"
"\n"
"\n"
"padding:3px;\n"
"padding-bottom:10px;")
        self.Ejemplo_Imagen.setText("")
        self.Ejemplo_Imagen.setScaledContents(True)
        self.Ejemplo_Imagen.setWordWrap(True)
        self.verticalLayout_7.addWidget(self.Ejemplo_Imagen)

        file_extension = directorio.split(".")[-1]
        if file_extension == "jpg" or file_extension == "png" or file_extension == "jpeg":#Si es una imagen
            self.Ejemplo_Imagen.setMinimumSize(QtCore.QSize(200, 200))
            self.Ejemplo_Imagen.setMaximumSize(QtCore.QSize(300, 300))
            pixmap = QtGui.QPixmap(directorio)
            pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
            self.Ejemplo_Imagen.setPixmap(pixmap)
            self.Ejemplo_Imagen.setObjectName("ejemplo_imagen")
            self.verticalLayout_7.addWidget(self.Ejemplo_Imagen)

            
        else:
            _translate = QtCore.QCoreApplication.translate
            self.Ejemplo_Imagen.setText(_translate("Dialog", directorio.split("/")[-1]))
        
        self.Ejemplo_Imagen.setObjectName("ejemplo_imagen")
        self.verticalLayout_7.addWidget(self.Ejemplo_Imagen)

        contenidos_de_scroll.append("")#Asi lo hacemos para guardarlo en la lista y diferenciarlo
        lista_solo_para_remove.append(self.Ejemplo_Imagen)
        

    def poner_todo_bien(self):
        global contenidos_de_scroll, mensaje_entero
        i = 0
        for contenido in contenidos_de_scroll: #Aqui simplemente updeteamos mensaje_entero por si acaso ha cambiado algo

            if contenido != "":
                text = contenido.toPlainText()
                mensaje_entero[i][1] = (text,)

            i += 1

        print(mensaje_entero)

    def enviar_a_contacto(self):

        global nombres, EasySend, mensaje_entero


        self.progressBar.setMaximum(len(nombres))



        z = threading.Thread(daemon=True, target=EasySend.mandar_a_todo_el_mundo, args=(nombres, mensaje_entero, self))
        z.start()
        self.stackedWidget.setCurrentIndex(8)


    






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
