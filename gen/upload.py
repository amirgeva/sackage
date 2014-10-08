# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/upload.ui'
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
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 384, 113, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 113, 33))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.userEdit = QtGui.QLineEdit(Dialog)
        Dialog.userEdit.setGeometry(QtCore.QRect(272, 16, 161, 32))
        Dialog.userEdit.setObjectName(_fromUtf8("userEdit"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 225, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(16, 64, 84, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.ppaEdit = QtGui.QLineEdit(Dialog)
        Dialog.ppaEdit.setGeometry(QtCore.QRect(272, 64, 161, 32))
        Dialog.ppaEdit.setObjectName(_fromUtf8("ppaEdit"))
        Dialog.outputEdit = QtGui.QPlainTextEdit(Dialog)
        Dialog.outputEdit.setGeometry(QtCore.QRect(16, 208, 481, 257))
        Dialog.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 176, 84, 22))
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.uploadButton = QtGui.QPushButton(Dialog)
        Dialog.uploadButton.setGeometry(QtCore.QRect(288, 112, 119, 32))
        Dialog.uploadButton.setObjectName(_fromUtf8("uploadButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Upload to Launchpad", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Close", None))
        Dialog.nextButton.setText(_translate("Dialog", "Done", None))
        Dialog.label.setText(_translate("Dialog", "Launchpad User Name:", None))
        Dialog.label_2.setText(_translate("Dialog", "PPA:", None))
        Dialog.label_3.setText(_translate("Dialog", "Output", None))
        Dialog.uploadButton.setText(_translate("Dialog", "Upload", None))

