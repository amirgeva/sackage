# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/ignore.ui'
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
        Dialog.removeButton = QtGui.QPushButton(Dialog)
        Dialog.removeButton.setGeometry(QtCore.QRect(144, 384, 119, 32))
        Dialog.removeButton.setAutoDefault(False)
        Dialog.removeButton.setObjectName(_fromUtf8("removeButton"))
        Dialog.label_4 = QtGui.QLabel(Dialog)
        Dialog.label_4.setGeometry(QtCore.QRect(16, 128, 113, 22))
        Dialog.label_4.setObjectName(_fromUtf8("label_4"))
        Dialog.addButton = QtGui.QPushButton(Dialog)
        Dialog.addButton.setGeometry(QtCore.QRect(16, 384, 119, 32))
        Dialog.addButton.setAutoDefault(False)
        Dialog.addButton.setObjectName(_fromUtf8("addButton"))
        Dialog.ignoreList = QtGui.QListWidget(Dialog)
        Dialog.ignoreList.setGeometry(QtCore.QRect(16, 160, 256, 209))
        Dialog.ignoreList.setObjectName(_fromUtf8("ignoreList"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 16, 609, 97))
        Dialog.label_3.setWordWrap(True)
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.prevButton = QtGui.QPushButton(Dialog)
        Dialog.prevButton.setGeometry(QtCore.QRect(512, 384, 119, 32))
        Dialog.prevButton.setAutoDefault(False)
        Dialog.prevButton.setObjectName(_fromUtf8("prevButton"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 336, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Ignore Patterns", None))
        Dialog.removeButton.setText(_translate("Dialog", "Remove", None))
        Dialog.label_4.setText(_translate("Dialog", "Ignore List", None))
        Dialog.addButton.setText(_translate("Dialog", "Add", None))
        Dialog.label_3.setText(_translate("Dialog", "Specify any file name pattern that should not be packaged.   For example, in python projects,  *.pyc", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))

