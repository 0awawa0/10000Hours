# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notes_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 303))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.notesLayout = QtWidgets.QVBoxLayout()
        self.notesLayout.setObjectName("notesLayout")
        self.verticalLayout_3.addLayout(self.notesLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEditAdd = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditAdd.sizePolicy().hasHeightForWidth())
        self.textEditAdd.setSizePolicy(sizePolicy)
        self.textEditAdd.setObjectName("textEditAdd")
        self.horizontalLayout.addWidget(self.textEditAdd)
        self.btnAdd = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditDelete = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditDelete.setInputMask("")
        self.lineEditDelete.setObjectName("lineEditDelete")
        self.horizontalLayout_2.addWidget(self.lineEditDelete)
        self.btnDelete = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notes"))
        self.textEditAdd.setPlaceholderText(_translate("MainWindow", "Enter note text"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Deleting provided using note ID"))
        self.lineEditDelete.setPlaceholderText(_translate("MainWindow", "Enter note ID"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))

