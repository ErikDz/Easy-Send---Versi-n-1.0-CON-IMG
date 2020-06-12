from PyQt5 import QtCore, QtGui, QtWidgets
class introducieno_email:

    def __init__(self, object):

        object.introducieno_email = QtWidgets.QWidget()
        object.introducieno_email.setObjectName("introducieno_email")
        object.gridLayout_10 = QtWidgets.QGridLayout(object.introducieno_email)
        object.gridLayout_10.setObjectName("gridLayout_10")
        object.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_14.addItem(spacerItem14)
        object.pushButton_confirmarContinuar_ELEMAIL = QtWidgets.QPushButton(object.introducieno_email)
        object.pushButton_confirmarContinuar_ELEMAIL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        object.pushButton_confirmarContinuar_ELEMAIL.setStyleSheet("border-radius: 19px;\n"
"border: 4px solid #77D7C8;\n"
"padding: 10px;\n"
"padding-right:50px;\n"
"padding-left:50px;\n"
"\n"
"font-size: 15px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif\n"
"")
        object.pushButton_confirmarContinuar_ELEMAIL.setObjectName("pushButton_confirmarContinuar_ELEMAIL")
        object.pushButton_confirmarContinuar_ELEMAIL.clicked.connect(object.is_clicked_confirmar_email)
        object.horizontalLayout_14.addWidget(object.pushButton_confirmarContinuar_ELEMAIL)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_14.addItem(spacerItem15)
        object.gridLayout_10.addLayout(object.horizontalLayout_14, 4, 0, 1, 1)
        object.lineEdit_entrar_email = QtWidgets.QLineEdit(object.introducieno_email)
        object.lineEdit_entrar_email.setStyleSheet("border-radius: 19px;\n"
"border: 1px solid #707070;\n"
"padding: 10px;\n"
"margin-top: 25px;\n"
"margin-bottom: 0px;\n"
"margin-right: 300px;\n"
"margin-left: 300px;\n"
"\n"
"font-family:\"Segoe UI\";")
        object.lineEdit_entrar_email.setAlignment(QtCore.Qt.AlignCenter)
        object.lineEdit_entrar_email.setObjectName("lineEdit_entrar_email")
        object.gridLayout_10.addWidget(object.lineEdit_entrar_email, 1, 0, 1, 1)
        object.label_6 = QtWidgets.QLabel(object.introducieno_email)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_6.sizePolicy().hasHeightForWidth())
        object.label_6.setSizePolicy(sizePolicy)
        object.label_6.setStyleSheet("font-size: 20px;\n"
"color: #707070;\n"
"font-family:\"Segoe UI\";\n"
"margin-bottom:60px;\n"
"margin-top:60px;\n"
"font-weight: 20;")
        object.label_6.setAlignment(QtCore.Qt.AlignCenter)
        object.label_6.setObjectName("label_6")
        object.gridLayout_10.addWidget(object.label_6, 2, 0, 1, 1)
        object.label_5 = QtWidgets.QLabel(object.introducieno_email)
        object.label_5.setStyleSheet("font-size: 25px;\n"
"margin-top:200px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_5.setAlignment(QtCore.Qt.AlignCenter)
        object.label_5.setObjectName("label_5")
        object.gridLayout_10.addWidget(object.label_5, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        object.gridLayout_10.addItem(spacerItem16, 3, 0, 1, 1)
        object.stackedWidget.addWidget(object.introducieno_email)



















