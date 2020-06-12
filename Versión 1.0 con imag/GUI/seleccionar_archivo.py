from PyQt5 import QtCore, QtGui, QtWidgets
class seleccionar_archivo:

    def __init__(self, object):

        object.Seleccionar_archivo = QtWidgets.QWidget()
        object.Seleccionar_archivo.setObjectName("Seleccionar_archivo")
        object.gridLayout_3 = QtWidgets.QGridLayout(object.Seleccionar_archivo)
        object.gridLayout_3.setObjectName("gridLayout_3")
        object.label_4 = QtWidgets.QLabel(object.Seleccionar_archivo)
        object.label_4.setStyleSheet("font-size: 25px;\n"
"margin-top:200px;\n"
"color: #1CB39B;\n"
"font-family: \"Segoe UI\";")
        object.label_4.setAlignment(QtCore.Qt.AlignCenter)
        object.label_4.setObjectName("label_4")
        object.gridLayout_3.addWidget(object.label_4, 1, 0, 1, 1)
        object.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_7.addItem(spacerItem4)
        object.pushButton_ConfirmarContinuar_buscar_archivo = QtWidgets.QPushButton(object.Seleccionar_archivo)
        object.pushButton_ConfirmarContinuar_buscar_archivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_ConfirmarContinuar_buscar_archivo.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.pushButton_ConfirmarContinuar_buscar_archivo.setObjectName("pushButton_ConfirmarContinuar_buscar_archivo")
        object.pushButton_ConfirmarContinuar_buscar_archivo.clicked.connect(object.is_clicked_confirmar_archivo)
        object.horizontalLayout_7.addWidget(object.pushButton_ConfirmarContinuar_buscar_archivo)
        object.gridLayout_3.addLayout(object.horizontalLayout_7, 7, 0, 1, 1)
        object.label_que_has_seleccionado = QtWidgets.QLabel(object.Seleccionar_archivo)
        object.label_que_has_seleccionado.setStyleSheet("font-size: 20px;\n"
"color: #707070;\n"
"font-family: \"Segoe UI\";rif;\n"
"margin-bottom:60px;\n"
"font-weight: 20;")
        object.label_que_has_seleccionado.setAlignment(QtCore.Qt.AlignCenter)
        object.label_que_has_seleccionado.setObjectName("label_que_has_seleccionado")
        object.gridLayout_3.addWidget(object.label_que_has_seleccionado, 5, 0, 1, 1)
        object.label_Error = QtWidgets.QLabel(object.Seleccionar_archivo)
        object.label_Error.setStyleSheet("font-size: 20px;\n"
"color: rgb(255, 0, 4);\n"
"font-family: \"Segoe UI\";\n"
"margin-bottom:60px;\n"
"font-weight: 20;")
        object.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        object.label_Error.setObjectName("label_Error")
        object.gridLayout_3.addWidget(object.label_Error, 6, 0, 1, 1)
        object.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_13.addItem(spacerItem5)
        object.pushButton_buscar_archivo_contactos = QtWidgets.QPushButton(object.Seleccionar_archivo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_buscar_archivo_contactos.sizePolicy().hasHeightForWidth())
        object.pushButton_buscar_archivo_contactos.setSizePolicy(sizePolicy)
        object.pushButton_buscar_archivo_contactos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_buscar_archivo_contactos.setMouseTracking(False)
        object.pushButton_buscar_archivo_contactos.setAcceptDrops(False)
        object.pushButton_buscar_archivo_contactos.setStyleSheet("\n"
"\n"
"margin-top: 10px;\n"
"\n"
"border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 6px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: \"Segoe UI\";")
        object.pushButton_buscar_archivo_contactos.setObjectName("pushButton_buscar_archivo_contactos")
        object.pushButton_buscar_archivo_contactos.clicked.connect(object.is_clicked_seleccionar_archivo)
        object.horizontalLayout_13.addWidget(object.pushButton_buscar_archivo_contactos)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_13.addItem(spacerItem6)
        object.gridLayout_3.addLayout(object.horizontalLayout_13, 3, 0, 1, 1)
        object.stackedWidget.addWidget(object.Seleccionar_archivo)



