from PyQt5 import QtCore, QtGui, QtWidgets
class seleccionar_columnas:

    def __init__(self, object):

        object.Seleccionar_Columnas = QtWidgets.QWidget()
        object.Seleccionar_Columnas.setObjectName("Seleccionar_Columnas")
        object.gridLayout_4 = QtWidgets.QGridLayout(object.Seleccionar_Columnas)
        object.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.gridLayout_4.addItem(spacerItem7, 6, 0, 1, 1)
        object.label_encontrado_siguientes_campos = QtWidgets.QLabel(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_encontrado_siguientes_campos.sizePolicy().hasHeightForWidth())
        object.label_encontrado_siguientes_campos.setSizePolicy(sizePolicy)
        object.label_encontrado_siguientes_campos.setStyleSheet("font-size: 25px;\n"
"margin-top:50px;\n"
"\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_encontrado_siguientes_campos.setObjectName("label_encontrado_siguientes_campos")
        object.gridLayout_4.addWidget(object.label_encontrado_siguientes_campos, 0, 0, 1, 1)
        object.verticalLayout_4 = QtWidgets.QVBoxLayout()
        object.verticalLayout_4.setObjectName("verticalLayout_4")
        object.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_2.setObjectName("horizontalLayout_2")
        object.label_10 = QtWidgets.QLabel(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_10.sizePolicy().hasHeightForWidth())
        object.label_10.setSizePolicy(sizePolicy)
        object.label_10.setStyleSheet("font-size: 25px;\n"
"\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.label_10.setObjectName("label_10")
        object.horizontalLayout_2.addWidget(object.label_10)
        object.verticalLayout_5 = QtWidgets.QVBoxLayout()
        object.verticalLayout_5.setObjectName("verticalLayout_5")
        object.comboBox_nombres = QtWidgets.QComboBox(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.comboBox_nombres.sizePolicy().hasHeightForWidth())
        object.comboBox_nombres.setSizePolicy(sizePolicy)
        object.comboBox_nombres.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.comboBox_nombres.setStyleSheet("\n"
"font-size: 20px;\n"
"border: 1px solid transparent;\n"
"border-color: #707070;\n"
"padding: 3px;\n"
"color: #707070;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif;\n"
"\n"
"font-weight: 20;")
        object.comboBox_nombres.setFrame(False)
        object.comboBox_nombres.setObjectName("comboBox_nombres")
        object.comboBox_nombres.addItem("")
        object.verticalLayout_5.addWidget(object.comboBox_nombres)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        object.verticalLayout_5.addItem(spacerItem8)
        object.horizontalLayout_2.addLayout(object.verticalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_2.addItem(spacerItem9)
        object.verticalLayout_4.addLayout(object.horizontalLayout_2)
        object.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_3.setObjectName("horizontalLayout_3")
        object.label_11 = QtWidgets.QLabel(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_11.sizePolicy().hasHeightForWidth())
        object.label_11.setSizePolicy(sizePolicy)
        object.label_11.setStyleSheet("font-size: 25px;\n"
"\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.label_11.setAlignment(QtCore.Qt.AlignCenter)
        object.label_11.setObjectName("label_11")
        object.horizontalLayout_3.addWidget(object.label_11)
        object.verticalLayout_10 = QtWidgets.QVBoxLayout()
        object.verticalLayout_10.setObjectName("verticalLayout_10")
        object.comboBox_telefonos = QtWidgets.QComboBox(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.comboBox_telefonos.sizePolicy().hasHeightForWidth())
        object.comboBox_telefonos.setSizePolicy(sizePolicy)
        object.comboBox_telefonos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.comboBox_telefonos.setStyleSheet("\n"
"font-size: 20px;\n"
"border: 1px solid transparent;\n"
"border-color: #707070;\n"
"padding: 3px;\n"
"color: #707070;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif;\n"
"\n"
"font-weight: 20;")
        object.comboBox_telefonos.setFrame(False)
        object.comboBox_telefonos.setObjectName("comboBox_telefonos")
        object.comboBox_telefonos.addItem("")
        object.verticalLayout_10.addWidget(object.comboBox_telefonos)
        spacerItem10 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        object.verticalLayout_10.addItem(spacerItem10)
        object.horizontalLayout_3.addLayout(object.verticalLayout_10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_3.addItem(spacerItem11)
        object.verticalLayout_4.addLayout(object.horizontalLayout_3)
        object.gridLayout_4.addLayout(object.verticalLayout_4, 4, 0, 1, 1)
        object.horizontalLayout = QtWidgets.QHBoxLayout()
        object.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout.addItem(spacerItem12)
        object.pushButton_confirmarContinuar_campos = QtWidgets.QPushButton(object.Seleccionar_Columnas)
        object.pushButton_confirmarContinuar_campos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_confirmarContinuar_campos.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family:\"Segoe UI\";")
        object.pushButton_confirmarContinuar_campos.setObjectName("pushButton_confirmarContinuar_campos")
        object.pushButton_confirmarContinuar_campos.clicked.connect(object.is_clicked_confirmar_columnas)
        object.horizontalLayout.addWidget(object.pushButton_confirmarContinuar_campos)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout.addItem(spacerItem13)
        object.gridLayout_4.addLayout(object.horizontalLayout, 5, 0, 1, 1)
        object.scrollArea_2 = QtWidgets.QScrollArea(object.Seleccionar_Columnas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.scrollArea_2.sizePolicy().hasHeightForWidth())
        object.scrollArea_2.setSizePolicy(sizePolicy)
        object.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        object.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        object.scrollArea_2.setWidgetResizable(True)
        object.scrollArea_2.setObjectName("scrollArea_2")
        object.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        object.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1090, 80))
        object.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        object.verticalLayout_3 = QtWidgets.QVBoxLayout(object.scrollAreaWidgetContents_2)
        object.verticalLayout_3.setObjectName("verticalLayout_3")


        object.scrollArea_2.setWidget(object.scrollAreaWidgetContents_2)
        object.gridLayout_4.addWidget(object.scrollArea_2, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        object.gridLayout_4.addItem(spacerItem14, 3, 0, 1, 1)

        object.stackedWidget.addWidget(object.Seleccionar_Columnas)