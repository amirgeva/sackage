# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/pkginfo.ui'
#
#
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        Dialog.prevButton = QtGui.QPushButton(Dialog)
        Dialog.prevButton.setGeometry(QtCore.QRect(512, 384, 119, 32))
        Dialog.prevButton.setAutoDefault(False)
        Dialog.prevButton.setObjectName(_fromUtf8("prevButton"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 336, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.sectionCB = QtGui.QComboBox(Dialog)
        Dialog.sectionCB.setGeometry(QtCore.QRect(192, 16, 337, 32))
        Dialog.sectionCB.setObjectName(_fromUtf8("sectionCB"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(16, 64, 84, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.priorityCB = QtGui.QComboBox(Dialog)
        Dialog.priorityCB.setGeometry(QtCore.QRect(192, 64, 337, 32))
        Dialog.priorityCB.setObjectName(_fromUtf8("priorityCB"))
        Dialog.priorityCB.addItem(_fromUtf8(""))
        Dialog.priorityCB.addItem(_fromUtf8(""))
        Dialog.priorityCB.addItem(_fromUtf8(""))
        Dialog.priorityCB.addItem(_fromUtf8(""))
        Dialog.priorityCB.addItem(_fromUtf8(""))
        Dialog.shortDescEdit = QtGui.QLineEdit(Dialog)
        Dialog.shortDescEdit.setGeometry(QtCore.QRect(192, 112, 433, 32))
        Dialog.shortDescEdit.setObjectName(_fromUtf8("shortDescEdit"))
        Dialog.dependList = QtGui.QListWidget(Dialog)
        Dialog.dependList.setGeometry(QtCore.QRect(192, 272, 256, 193))
        Dialog.dependList.setObjectName(_fromUtf8("dependList"))
        Dialog.longDescEdit = QtGui.QPlainTextEdit(Dialog)
        Dialog.longDescEdit.setGeometry(QtCore.QRect(192, 160, 433, 97))
        Dialog.longDescEdit.setObjectName(_fromUtf8("longDescEdit"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 112, 177, 22))
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.label_4 = QtGui.QLabel(Dialog)
        Dialog.label_4.setGeometry(QtCore.QRect(16, 160, 161, 22))
        Dialog.label_4.setObjectName(_fromUtf8("label_4"))
        Dialog.label_5 = QtGui.QLabel(Dialog)
        Dialog.label_5.setGeometry(QtCore.QRect(16, 272, 145, 32))
        Dialog.label_5.setObjectName(_fromUtf8("label_5"))
        Dialog.pushButton = QtGui.QPushButton(Dialog)
        Dialog.pushButton.setGeometry(QtCore.QRect(80, 336, 97, 32))
        Dialog.pushButton.setObjectName(_fromUtf8("pushButton"))
        Dialog.pushButton_2 = QtGui.QPushButton(Dialog)
        Dialog.pushButton_2.setGeometry(QtCore.QRect(80, 384, 97, 32))
        Dialog.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Package Information", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.label.setText(_translate("Dialog", "Section:", None))
        Dialog.label_2.setText(_translate("Dialog", "Priority:", None))
        Dialog.priorityCB.setItemText(0, _translate("Dialog", "standard", None))
        Dialog.priorityCB.setItemText(1, _translate("Dialog", "required", None))
        Dialog.priorityCB.setItemText(2, _translate("Dialog", "important", None))
        Dialog.priorityCB.setItemText(3, _translate("Dialog", "optional", None))
        Dialog.priorityCB.setItemText(4, _translate("Dialog", "extra", None))
        Dialog.label_3.setText(_translate("Dialog", "Short Description:", None))
        Dialog.label_4.setText(_translate("Dialog", "Long Description:", None))
        Dialog.label_5.setText(_translate("Dialog", "Dependencies:", None))
        Dialog.pushButton.setText(_translate("Dialog", "Add", None))
        Dialog.pushButton_2.setText(_translate("Dialog", "Remove", None))

