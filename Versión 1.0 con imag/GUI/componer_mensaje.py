from PyQt5 import QtCore, QtGui, QtWidgets
class componer_mensaje:

    def __init__(self, object):

        object.Componer_Mensaje = QtWidgets.QWidget()
        object.Componer_Mensaje.setObjectName("Componer_Mensaje")
        object.gridLayout_7 = QtWidgets.QGridLayout(object.Componer_Mensaje)
        object.gridLayout_7.setObjectName("gridLayout_7")
        object.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_16.addItem(spacerItem24)
        object.pushButton_ConfirmarMensajeComponer = QtWidgets.QPushButton(object.Componer_Mensaje)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_ConfirmarMensajeComponer.sizePolicy().hasHeightForWidth())
        object.pushButton_ConfirmarMensajeComponer.setSizePolicy(sizePolicy)
        object.pushButton_ConfirmarMensajeComponer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_ConfirmarMensajeComponer.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";\n"
"")
        object.pushButton_ConfirmarMensajeComponer.setObjectName("pushButton_ConfirmarMensajeComponer")
        object.pushButton_ConfirmarMensajeComponer.clicked.connect(object.is_clicked_finalizar_componer)
        object.horizontalLayout_16.addWidget(object.pushButton_ConfirmarMensajeComponer)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_16.addItem(spacerItem25)
        object.gridLayout_7.addLayout(object.horizontalLayout_16, 3, 0, 1, 1)
        object.label_13 = QtWidgets.QLabel(object.Componer_Mensaje)
        object.label_13.setStyleSheet("font-size: 25px;\n"
"\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_13.setObjectName("label_13")
        object.gridLayout_7.addWidget(object.label_13, 0, 0, 1, 1)
        object.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_9.setObjectName("horizontalLayout_9")
        object.label_20 = QtWidgets.QLabel(object.Componer_Mensaje)
        object.label_20.setStyleSheet("font-size: 24px;\n"
"color: #707070;\n"
"font-family:\"Segoe UI\";\n"
"margin-bottom:60px;\n"
"font-weight: 400;")
        object.label_20.setObjectName("label_20")
        object.horizontalLayout_9.addWidget(object.label_20)
        object.gridLayout_7.addLayout(object.horizontalLayout_9, 2, 0, 1, 1)
        object.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_4.setObjectName("horizontalLayout_4")
        object.verticalLayout_2 = QtWidgets.QVBoxLayout()
        object.verticalLayout_2.setObjectName("verticalLayout_2")
        object.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_5.setObjectName("horizontalLayout_5")
        object.plainTextEdit_hacer_mensaje = QtWidgets.QPlainTextEdit(object.Componer_Mensaje)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.plainTextEdit_hacer_mensaje.sizePolicy().hasHeightForWidth())
        object.plainTextEdit_hacer_mensaje.setSizePolicy(sizePolicy)
        object.plainTextEdit_hacer_mensaje.setMinimumSize(QtCore.QSize(400, 260))
        object.plainTextEdit_hacer_mensaje.setStyleSheet("margin-top:50px;\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"color: #707070;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif;\n"
"\n"
"font-weight: 20;")
        object.plainTextEdit_hacer_mensaje.setPlainText("")
        object.plainTextEdit_hacer_mensaje.setOverwriteMode(True)
        object.plainTextEdit_hacer_mensaje.setObjectName("plainTextEdit_hacer_mensaje")
        object.horizontalLayout_5.addWidget(object.plainTextEdit_hacer_mensaje)
        object.pushButton_AgregarMensaje = QtWidgets.QPushButton(object.Componer_Mensaje)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_AgregarMensaje.sizePolicy().hasHeightForWidth())
        object.pushButton_AgregarMensaje.setSizePolicy(sizePolicy)
        object.pushButton_AgregarMensaje.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_AgregarMensaje.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"\n"
"padding-left:50px;\n"
"padding-right:50px;\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.pushButton_AgregarMensaje.setObjectName("pushButton_AgregarMensaje")
        object.pushButton_AgregarMensaje.clicked.connect(object.is_clicked_agregar_mensaje)
        object.horizontalLayout_5.addWidget(object.pushButton_AgregarMensaje)
        spacerItem26 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_5.addItem(spacerItem26)
        object.verticalLayout_2.addLayout(object.horizontalLayout_5)
        object.pushButton_AdjuntarUnArchivo = QtWidgets.QPushButton(object.Componer_Mensaje)
        object.pushButton_AdjuntarUnArchivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_AdjuntarUnArchivo.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"margin-right: 0px;\n"
"margin-left: 0px;\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.pushButton_AdjuntarUnArchivo.setObjectName("pushButton_AdjuntarUnArchivo")
        object.pushButton_AdjuntarUnArchivo.clicked.connect(object.is_clicked_agregar_imagen)
        object.verticalLayout_2.addWidget(object.pushButton_AdjuntarUnArchivo)
        spacerItem27 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.verticalLayout_2.addItem(spacerItem27)
        object.horizontalLayout_4.addLayout(object.verticalLayout_2)
        object.verticalLayout = QtWidgets.QVBoxLayout()
        object.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        object.verticalLayout.setObjectName("verticalLayout")
        object.label_19 = QtWidgets.QLabel(object.Componer_Mensaje)
        object.label_19.setStyleSheet("font-size: 25px;\n"
"\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.label_19.setObjectName("label_19")
        object.verticalLayout.addWidget(object.label_19)
        object.scrollArea = QtWidgets.QScrollArea(object.Componer_Mensaje)
        object.scrollArea.setLayoutDirection(QtCore.Qt.RightToLeft)
        object.scrollArea.setStyleSheet("background:rgb(242, 249, 255);\n"
"\n"
"")
        object.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        object.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        object.scrollArea.setLineWidth(1)
        object.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        object.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        object.scrollArea.setWidgetResizable(True)
        object.scrollArea.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        object.scrollArea.setObjectName("scrollArea")
        object.scrollAreaWidgetContents = QtWidgets.QWidget()
        object.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 416, 438))
        object.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        object.horizontalLayout_10 = QtWidgets.QHBoxLayout(object.scrollAreaWidgetContents)
        object.horizontalLayout_10.setObjectName("horizontalLayout_10")
        object.verticalLayout_7 = QtWidgets.QVBoxLayout()
        object.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem28 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        object.verticalLayout_7.addItem(spacerItem28)
        object.horizontalLayout_10.addLayout(object.verticalLayout_7)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_10.addItem(spacerItem29)
        object.scrollArea.setWidget(object.scrollAreaWidgetContents)
        object.verticalLayout.addWidget(object.scrollArea)




        object.label_21 = QtWidgets.QLabel(object.Componer_Mensaje)
        object.label_21.setStyleSheet("font-size: 20px;\n"
"color: #707070;\n"
"font-family:\"Segoe UI\";\n"
"\n"
"font-weight: 400;")
        object.label_21.setObjectName("label_21")
        object.verticalLayout.addWidget(object.label_21)
        object.horizontalLayout_4.addLayout(object.verticalLayout)
        object.gridLayout_7.addLayout(object.horizontalLayout_4, 1, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.gridLayout_7.addItem(spacerItem30, 4, 0, 1, 1)
        object.stackedWidget.addWidget(object.Componer_Mensaje)

