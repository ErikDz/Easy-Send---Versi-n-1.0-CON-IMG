#enviando_progreso

from PyQt5 import QtCore, QtGui, QtWidgets
from os import getcwd
class enviando_progreso:

    def __init__(self, object):
        object.enviando_progreso = QtWidgets.QWidget()
        object.enviando_progreso.setObjectName("enviando_progreso")
        object.gridLayout_9 = QtWidgets.QGridLayout(object.enviando_progreso)
        object.gridLayout_9.setObjectName("gridLayout_9")
        object.label_Imagenes_MovilOrdenata = QtWidgets.QLabel(object.enviando_progreso)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_Imagenes_MovilOrdenata.sizePolicy().hasHeightForWidth())
        object.label_Imagenes_MovilOrdenata.setSizePolicy(sizePolicy)
        object.label_Imagenes_MovilOrdenata.setAlignment(QtCore.Qt.AlignCenter)
        object.label_Imagenes_MovilOrdenata.setObjectName("label_Imagenes_MovilOrdenata")
        pixmap = QtGui.QPixmap(getcwd()+"\\img\\progress.png")
        object.label_Imagenes_MovilOrdenata.setPixmap(pixmap)


        object.gridLayout_9.addWidget(object.label_Imagenes_MovilOrdenata, 4, 0, 1, 1)
        object.label_23 = QtWidgets.QLabel(object.enviando_progreso)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_23.sizePolicy().hasHeightForWidth())
        object.label_23.setSizePolicy(sizePolicy)
        object.label_23.setStyleSheet("font-size: 25px;\n"
"margin-top:200px;\n"
"color: #1CB39B;\n"
"font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen, Ubuntu, Cantarell, \"Open Sans\", \"Helvetica Neue\", sans-serif")
        object.label_23.setAlignment(QtCore.Qt.AlignCenter)
        object.label_23.setObjectName("label_23")
        object.gridLayout_9.addWidget(object.label_23, 1, 0, 1, 1)
        object.label_25 = QtWidgets.QLabel(object.enviando_progreso)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.label_25.sizePolicy().hasHeightForWidth())
        object.label_25.setSizePolicy(sizePolicy)
        object.label_25.setStyleSheet("font-size: 26px;\n"
"color: #707070;\n"
"font-family:\"Segoe UI\";\n"
"\n"
"font-weight: 400;")
        object.label_25.setAlignment(QtCore.Qt.AlignCenter)
        object.label_25.setObjectName("label_25")
        object.gridLayout_9.addWidget(object.label_25, 5, 0, 1, 1)
        object.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        object.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        object.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem34 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_12.addItem(spacerItem34)
        object.progressBar = QtWidgets.QProgressBar(object.enviando_progreso)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.progressBar.sizePolicy().hasHeightForWidth())
        object.progressBar.setSizePolicy(sizePolicy)
        object.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        object.progressBar.setStyleSheet("\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 12px;\n"
"    \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"   border-radius: 10px;\n"
"   border: 2px solid #1CB39B;\n"
"   background: #1CB39B;\n"
"\n"
"}\n"
"\n"
"")
        object.progressBar.setMinimum(0)
        object.progressBar.setMaximum(100)
        object.progressBar.setProperty("value", 24)
        object.progressBar.setTextVisible(False)
        object.progressBar.setInvertedAppearance(False)
        object.progressBar.setObjectName("progressBar")
        object.horizontalLayout_12.addWidget(object.progressBar)
        spacerItem35 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        object.horizontalLayout_12.addItem(spacerItem35)
        object.gridLayout_9.addLayout(object.horizontalLayout_12, 2, 0, 1, 1)
        object.stackedWidget.addWidget(object.enviando_progreso)

