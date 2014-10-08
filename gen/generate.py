# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/generate.ui'
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
        Dialog.label.setGeometry(QtCore.QRect(16, 0, 369, 65))
        Dialog.label.setWordWrap(True)
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.generateButton = QtGui.QPushButton(Dialog)
        Dialog.generateButton.setGeometry(QtCore.QRect(400, 16, 193, 49))
        Dialog.generateButton.setObjectName(_fromUtf8("generateButton"))
        Dialog.outputEdit = QtGui.QPlainTextEdit(Dialog)
        Dialog.outputEdit.setGeometry(QtCore.QRect(16, 96, 609, 321))
        Dialog.outputEdit.setReadOnly(True)
        Dialog.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(384, 432, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(32, 64, 84, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Generate Package", None))
        Dialog.label.setText(_translate("Dialog", "All information has been collected. Click the button to generate the package", None))
        Dialog.generateButton.setText(_translate("Dialog", "Generate", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Close", None))
        Dialog.label_2.setText(_translate("Dialog", "Output", None))

