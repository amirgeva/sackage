# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/pkginfo2.ui'
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
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 32, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.comboBox = QtGui.QComboBox(Dialog)
        Dialog.comboBox.setGeometry(QtCore.QRect(160, 32, 241, 32))
        Dialog.comboBox.setObjectName(_fromUtf8("comboBox"))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))
        Dialog.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.label.setText(_translate("Dialog", "License:", None))
        Dialog.comboBox.setItemText(0, _translate("Dialog", "Apache-2.0", None))
        Dialog.comboBox.setItemText(1, _translate("Dialog", "BSD", None))
        Dialog.comboBox.setItemText(2, _translate("Dialog", "GFDL-1.2", None))
        Dialog.comboBox.setItemText(3, _translate("Dialog", "GFDL-1.3", None))
        Dialog.comboBox.setItemText(4, _translate("Dialog", "GPL-1", None))
        Dialog.comboBox.setItemText(5, _translate("Dialog", "GPL-2", None))
        Dialog.comboBox.setItemText(6, _translate("Dialog", "GPL-3", None))
        Dialog.comboBox.setItemText(7, _translate("Dialog", "LGPL-2", None))
        Dialog.comboBox.setItemText(8, _translate("Dialog", "LGPL-2.1", None))
        Dialog.comboBox.setItemText(9, _translate("Dialog", "LGPL-3", None))

