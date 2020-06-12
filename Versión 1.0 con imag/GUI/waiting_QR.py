from PyQt5 import QtCore, QtGui, QtWidgets
from os import getcwd
class waiting_QR:

    def __init__(self, object):



        object.Waiting_QR = QtWidgets.QWidget()
        object.Waiting_QR.setObjectName("Waiting_QR")
        object.gridLayout_6 = QtWidgets.QGridLayout(object.Waiting_QR)
        object.gridLayout_6.setObjectName("gridLayout_6")
        object.label_activar_QR = QtWidgets.QLabel(object.Waiting_QR)
        object.label_activar_QR.setMaximumSize(QtCore.QSize(16777214, 16777215))
        object.label_activar_QR.setObjectName("label_activar_QR")
        pixmap = QtGui.QPixmap(getcwd()+"\\img\\QR.jpg")
        #pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        object.label_activar_QR.setPixmap(pixmap)
        object.gridLayout_6.addWidget(object.label_activar_QR, 0, 0, 1, 1)
        object.stackedWidget.addWidget(object.Waiting_QR)