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
        Dialog.sectionCB.setGeometry(QtCore.QRect(160, 16, 337, 32))
        Dialog.sectionCB.setObjectName(_fromUtf8("sectionCB"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.label.setText(_translate("Dialog", "Section:", None))

