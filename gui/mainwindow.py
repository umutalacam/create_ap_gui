# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 225)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 190, 281, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 171))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 281, 124))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sourceComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sourceComboBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sharingComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sharingComboBox.setObjectName("sharingComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sharingComboBox)
        self.shareInternetCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.shareInternetCheckBox.setObjectName("shareInternetCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.shareInternetCheckBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 10, 301, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 281, 104))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ssidEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ssidEdit.setObjectName("ssidEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ssidEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.passwordEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setGeometry(QtCore.QRect(10, 100, 281, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.status_label = QtWidgets.QLabel(self.frame)
        self.status_label.setGeometry(QtCore.QRect(10, 10, 80, 20))
        self.status_label.setObjectName("status_label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Network Interface Settings"))
        self.label_2.setText(_translate("Dialog", "Sharing Interface"))
        self.shareInternetCheckBox.setText(_translate("Dialog", "Share Internet"))
        self.label.setText(_translate("Dialog", "Source Network"))
        self.groupBox_2.setTitle(_translate("Dialog", "WLAN Settings"))
        self.label_3.setText(_translate("Dialog", "SSID"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.status_label.setText(_translate("Dialog", "Status:"))


