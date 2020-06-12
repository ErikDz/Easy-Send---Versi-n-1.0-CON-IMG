#Diciendo_Que_Aada

from PyQt5 import QtCore, QtGui, QtWidgets
from os import getcwd
class Diciendo_Que_Aada:

    def __init__(self, object):

        object.Diciendo_Que_Aada = QtWidgets.QWidget()
        object.Diciendo_Que_Aada.setObjectName("Diciendo_Que_Aada")
        object.gridLayout_5 = QtWidgets.QGridLayout(object.Diciendo_Que_Aada)
        object.gridLayout_5.setObjectName("gridLayout_5")


        object.label_ImagenPantalla = QtWidgets.QLabel(object.Diciendo_Que_Aada)
        object.label_ImagenPantalla.setMinimumSize(QtCore.QSize(0, 500))
        object.label_ImagenPantalla.setObjectName("label_ImagenPantalla")
        object.gridLayout_5.addWidget(object.label_ImagenPantalla, 3, 1, 1, 1)
        pixmap = QtGui.QPixmap(getcwd()+"\\img\\contacts.jpg")
        #pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        object.label_ImagenPantalla.setPixmap(pixmap)




        object.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_8.addItem(spacerItem17)
        object.pushButton_Correo_No_recibido = QtWidgets.QPushButton(object.Diciendo_Que_Aada)
        object.pushButton_Correo_No_recibido.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_Correo_No_recibido.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: \"Segoe UI\";")
        object.pushButton_Correo_No_recibido.setObjectName("pushButton_Correo_No_recibido")
        object.pushButton_Correo_No_recibido.clicked.connect(object.is_clicked_correo_no_recibido)
        object.horizontalLayout_8.addWidget(object.pushButton_Correo_No_recibido)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_8.addItem(spacerItem18)
        object.pushButton_confirmarContinuar_correo = QtWidgets.QPushButton(object.Diciendo_Que_Aada)
        object.pushButton_confirmarContinuar_correo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_confirmarContinuar_correo.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif\n"
"")
        object.pushButton_confirmarContinuar_correo.setObjectName("pushButton_confirmarContinuar_correo")
        object.pushButton_confirmarContinuar_correo.clicked.connect(object.is_clicked_confirmar_agregado_contactos)
        object.horizontalLayout_8.addWidget(object.pushButton_confirmarContinuar_correo)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_8.addItem(spacerItem19)
        object.gridLayout_5.addLayout(object.horizontalLayout_8, 5, 1, 1, 1)
        object.label_12 = QtWidgets.QLabel(object.Diciendo_Que_Aada)
        object.label_12.setStyleSheet("font-size: 25px;\n"
"margin-top:0px;\n"
"margin-left:50px;\n"
"\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_12.setLineWidth(0)
        object.label_12.setObjectName("label_12")
        object.gridLayout_5.addWidget(object.label_12, 0, 1, 1, 1)
        object.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem20 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_15.addItem(spacerItem20)
        object.label_9 = QtWidgets.QLabel(object.Diciendo_Que_Aada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_9.sizePolicy().hasHeightForWidth())
        object.label_9.setSizePolicy(sizePolicy)
        object.label_9.setStyleSheet("font-size: 25px;\n"
"\n"
"\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_9.setObjectName("label_9")
        object.horizontalLayout_15.addWidget(object.label_9)
        object.label_donde_recibido_email = QtWidgets.QLabel(object.Diciendo_Que_Aada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_donde_recibido_email.sizePolicy().hasHeightForWidth())
        object.label_donde_recibido_email.setSizePolicy(sizePolicy)
        object.label_donde_recibido_email.setMinimumSize(QtCore.QSize(3, 0))
        object.label_donde_recibido_email.setStyleSheet("font-size: 25px;\n"
"\n"
"\n"
"color: rgb(61, 148, 255);\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_donde_recibido_email.setObjectName("label_donde_recibido_email")
        object.horizontalLayout_15.addWidget(object.label_donde_recibido_email)
        object.label_14 = QtWidgets.QLabel(object.Diciendo_Que_Aada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_14.sizePolicy().hasHeightForWidth())
        object.label_14.setSizePolicy(sizePolicy)
        object.label_14.setStyleSheet("font-size: 25px;\n"
"\n"
"\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_14.setObjectName("label_14")
        object.horizontalLayout_15.addWidget(object.label_14)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_15.addItem(spacerItem21)
        object.gridLayout_5.addLayout(object.horizontalLayout_15, 2, 1, 1, 1)
        object.stackedWidget.addWidget(object.Diciendo_Que_Aada)