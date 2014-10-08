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
        Dialog.label.setGeometry(QtCore.QRect(160, 16, 369, 97))
        Dialog.label.setWordWrap(True)
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.generateButton = QtGui.QPushButton(Dialog)
        Dialog.generateButton.setGeometry(QtCore.QRect(224, 192, 193, 97))
        Dialog.generateButton.setObjectName(_fromUtf8("generateButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Generate Package", None))
        Dialog.label.setText(_translate("Dialog", "All information has been collected. Click the button to generate the package", None))
        Dialog.generateButton.setText(_translate("Dialog", "Generate", None))

