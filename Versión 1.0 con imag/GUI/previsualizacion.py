#previsualizacion

from PyQt5 import QtCore, QtGui, QtWidgets
class previsualizacion:

    def __init__(self, object):

        object.previsualizacion = QtWidgets.QWidget()
        object.previsualizacion.setObjectName("previsualizacion")
        object.gridLayout_8 = QtWidgets.QGridLayout(object.previsualizacion)
        object.gridLayout_8.setObjectName("gridLayout_8")
        object.label_22 = QtWidgets.QLabel(object.previsualizacion)
        object.label_22.setStyleSheet("font-size: 25px;\n"
"margin-top:50px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_22.setAlignment(QtCore.Qt.AlignCenter)
        object.label_22.setObjectName("label_22")
        object.gridLayout_8.addWidget(object.label_22, 0, 0, 1, 1)
        object.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_11.setObjectName("horizontalLayout_11")
        object.verticalLayout_9 = QtWidgets.QVBoxLayout()
        object.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem29 = QtWidgets.QSpacerItem(40, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.verticalLayout_9.addItem(spacerItem29)
        object.pushButton_ReHacer = QtWidgets.QPushButton(object.previsualizacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_ReHacer.sizePolicy().hasHeightForWidth())
        object.pushButton_ReHacer.setSizePolicy(sizePolicy)
        object.pushButton_ReHacer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_ReHacer.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif\n"
"")
        object.pushButton_ReHacer.setObjectName("pushButton_ReHacer")
        object.pushButton_ReHacer.clicked.connect(object.is_clicked_re_hacer)
        object.verticalLayout_9.addWidget(object.pushButton_ReHacer)
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.verticalLayout_9.addItem(spacerItem30)
        object.horizontalLayout_11.addLayout(object.verticalLayout_9)





        """
        object.scrollArea_Previsualizar = QtWidgets.QScrollArea(object.previsualizacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.scrollArea_Previsualizar.sizePolicy().hasHeightForWidth())
        object.scrollArea_Previsualizar.setSizePolicy(sizePolicy)
        object.scrollArea_Previsualizar.setStyleSheet("margin-bottom:75px;")
        object.scrollArea_Previsualizar.setWidgetResizable(True)
        object.scrollArea_Previsualizar.setObjectName("scrollArea_Previsualizar")
        object.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        object.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 202, 442))
        object.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        object.scrollArea_Previsualizar.setWidget(object.scrollAreaWidgetContents_3)"""
        #object.horizontalLayout_11.addWidget(object.scrollArea_Previsualizar)
        










        object.verticalLayout_8 = QtWidgets.QVBoxLayout()
        object.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem31 = QtWidgets.QSpacerItem(40, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.verticalLayout_8.addItem(spacerItem31)
        object.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_17.addItem(spacerItem32)
        object.pushButton_ENVIAR = QtWidgets.QPushButton(object.previsualizacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.pushButton_ENVIAR.sizePolicy().hasHeightForWidth())
        object.pushButton_ENVIAR.setSizePolicy(sizePolicy)
        object.pushButton_ENVIAR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_ENVIAR.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif\n"
"")
        object.pushButton_ENVIAR.setObjectName("pushButton_ENVIAR")
        object.pushButton_ENVIAR.clicked.connect(object.is_clicked_enviar)
        object.horizontalLayout_17.addWidget(object.pushButton_ENVIAR)
        object.verticalLayout_8.addLayout(object.horizontalLayout_17)
        spacerItem33 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        object.verticalLayout_8.addItem(spacerItem33)
        object.horizontalLayout_11.addLayout(object.verticalLayout_8)
        object.gridLayout_8.addLayout(object.horizontalLayout_11, 1, 0, 1, 1)
        object.stackedWidget.addWidget(object.previsualizacion)