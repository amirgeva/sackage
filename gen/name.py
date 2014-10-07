# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/name.ui'
#
# Created: Tue Oct  7 21:51:04 2014
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
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(32, 128, 145, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(32, 0, 609, 97))
        Dialog.label_3.setWordWrap(True)
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.nameEdit = QtGui.QLineEdit(Dialog)
        Dialog.nameEdit.setGeometry(QtCore.QRect(192, 128, 257, 32))
        Dialog.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(32, 192, 145, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.emailEdit = QtGui.QLineEdit(Dialog)
        Dialog.emailEdit.setGeometry(QtCore.QRect(192, 192, 257, 32))
        Dialog.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        Dialog.label_4 = QtGui.QLabel(Dialog)
        Dialog.label_4.setGeometry(QtCore.QRect(32, 272, 401, 81))
        Dialog.label_4.setWordWrap(True)
        Dialog.label_4.setObjectName(_fromUtf8("label_4"))
        Dialog.bashrcButton = QtGui.QPushButton(Dialog)
        Dialog.bashrcButton.setGeometry(QtCore.QRect(32, 352, 161, 65))
        Dialog.bashrcButton.setAutoDefault(False)
        Dialog.bashrcButton.setObjectName(_fromUtf8("bashrcButton"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 384, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.label.setText(_translate("Dialog", "Your Name:", None))
        Dialog.label_3.setText(_translate("Dialog", "The details of the package maintainer / owner.", None))
        Dialog.label_2.setText(_translate("Dialog", "Your email:", None))
        Dialog.label_4.setText(_translate("Dialog", "Click this button to add environment variables DEBFULLNAME, DEBEMAIL  to your .bashrc", None))
        Dialog.bashrcButton.setText(_translate("Dialog", "Add to .bashrc", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))

