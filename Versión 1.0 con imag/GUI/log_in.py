from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from os import getcwd
class log_in:

    def __init__(self, object):
        object.Log_in = QtWidgets.QWidget()
        object.Log_in.setObjectName("Log_in")
        object.gridLayout_2 = QtWidgets.QGridLayout(object.Log_in)
        object.gridLayout_2.setObjectName("gridLayout_2")
        object.label_3 = QtWidgets.QLabel(object.Log_in)
        object.label_3.setStyleSheet("font-size: 20px;\n"
"color: #707070;\n"
"font-family: \"Segoe UI\";")
        object.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        object.label_3.setObjectName("label_3")
        object.gridLayout_2.addWidget(object.label_3, 5, 0, 1, 1)
        object.pushButton_Olvidado_contrasena = QtWidgets.QPushButton(object.Log_in)
        object.pushButton_Olvidado_contrasena.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_Olvidado_contrasena.setStyleSheet("font-size: 18px;\n"
"color: #1CB39B;\n"
"font-family: \"Segoe UI\";\n"
"")
        object.pushButton_Olvidado_contrasena.setAutoDefault(False)
        object.pushButton_Olvidado_contrasena.setFlat(True)
        object.pushButton_Olvidado_contrasena.setObjectName("pushButton_Olvidado_contrasena")
        object.gridLayout_2.addWidget(object.pushButton_Olvidado_contrasena, 9, 1, 1, 1)
        object.pushButton_LOGIN = QtWidgets.QPushButton(object.Log_in)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_LOGIN.sizePolicy().hasHeightForWidth())
        object.pushButton_LOGIN.setSizePolicy(sizePolicy)
        object.pushButton_LOGIN.setMinimumSize(QtCore.QSize(3, 0))
        object.pushButton_LOGIN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_LOGIN.setMouseTracking(True)
        object.pushButton_LOGIN.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 5px;\n"
"margin-right: 100px;\n"
"margin-left: 100px;\n"
"\n"
"font-size: 20px;\n"
"color: #1CB39B;\n"
"font-family: \"Segoe UI\";")
        object.pushButton_LOGIN.setObjectName("pushButton_LOGIN")
        object.pushButton_LOGIN.clicked.connect(object.log_in_ha_clickeado)
        object.gridLayout_2.addWidget(object.pushButton_LOGIN, 7, 1, 1, 1)
        object.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_6.setContentsMargins(-1, 100, -1, -1)
        object.horizontalLayout_6.setObjectName("horizontalLayout_6")
        object.label_LOGO = QtWidgets.QLabel(object.Log_in)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)



        sizePolicy.setHeightForWidth(object.label_LOGO.sizePolicy().hasHeightForWidth())
        object.label_LOGO.setSizePolicy(sizePolicy)
        object.label_LOGO.setMaximumSize(QtCore.QSize(100, 100))
        pixmap = QtGui.QPixmap(getcwd()+"\\img\\logo.jpg")
        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        object.label_LOGO.setPixmap(pixmap)
        object.label_LOGO.setScaledContents(True)
        object.label_LOGO.setObjectName("label_LOGO")
        object.horizontalLayout_6.addWidget(object.label_LOGO)





        object.gridLayout_2.addLayout(object.horizontalLayout_6, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.gridLayout_2.addItem(spacerItem, 3, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.gridLayout_2.addItem(spacerItem1, 10, 1, 1, 1)
        object.label_ErrorLogin = QtWidgets.QLabel(object.Log_in)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_ErrorLogin.sizePolicy().hasHeightForWidth())
        object.label_ErrorLogin.setSizePolicy(sizePolicy)
        object.label_ErrorLogin.setStyleSheet("font-size: 20px;\n"
"color: rgb(255, 0, 4);\n"
"font-family: \"Segoe UI\";\n"
"\n"
"font-weight: 20;")
        object.label_ErrorLogin.setAlignment(QtCore.Qt.AlignCenter)
        object.label_ErrorLogin.setObjectName("label_ErrorLogin")
        object.gridLayout_2.addWidget(object.label_ErrorLogin, 6, 1, 1, 1)
        object.label_2 = QtWidgets.QLabel(object.Log_in)
        object.label_2.setMouseTracking(True)
        object.label_2.setFocusPolicy(QtCore.Qt.TabFocus)
        object.label_2.setStyleSheet("margin-top: 10px;\n"
"margin-bottom: 6px;\n"
"font-size: 20px;\n"
"color: #707070;\n"
"font-family: \"Segoe UI\";")
        object.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        object.label_2.setObjectName("label_2")
        object.gridLayout_2.addWidget(object.label_2, 4, 0, 1, 1)
        object.lineEdit_Entrar_Usuario = QtWidgets.QLineEdit(object.Log_in)
        object.lineEdit_Entrar_Usuario.setStyleSheet("border-radius: 19px;\n"
"border: 1px solid #707070;\n"
"padding: 10px;\n"
"margin-top: 10px;\n"
"margin-bottom: 0px;\n"
"margin-right: 10px;\n"
"margin-left: 10px;\n"
"\n"
"font-family: \"Segoe UI\";\n")
        object.lineEdit_Entrar_Usuario.setObjectName("lineEdit_Entrar_Usuario")
        object.gridLayout_2.addWidget(object.lineEdit_Entrar_Usuario, 4, 1, 1, 1)
        object.label = QtWidgets.QLabel(object.Log_in)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label.sizePolicy().hasHeightForWidth())
        object.label.setSizePolicy(sizePolicy)
        object.label.setStyleSheet("font-family: \"Segoe UI\";\n"
"color: #707070;\n"
"font-size: 33px;\n"
"font-weight: 400;\n"
"line-height: 35px;\n"
"font-size: 30px;\n"
"margin-bottom: 100px;\n"
"")
        object.label.setAlignment(QtCore.Qt.AlignCenter)
        object.label.setObjectName("label")
        object.gridLayout_2.addWidget(object.label, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        object.lineEdit_Contrasena = QtWidgets.QLineEdit(object.Log_in)
        object.lineEdit_Contrasena.setStyleSheet("border-radius: 19px;\n"
"border: 1px solid #707070;\n"
"padding: 10px;\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"margin-right: 10px;\n"
"margin-left: 10px;\n"
"\n"
"font-family: \"Segoe UI\";\n")
        object.lineEdit_Contrasena.setObjectName("lineEdit_Contrasena")
        object.gridLayout_2.addWidget(object.lineEdit_Contrasena, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.gridLayout_2.addItem(spacerItem3, 8, 1, 1, 1)
        object.stackedWidget.addWidget(object.Log_in)