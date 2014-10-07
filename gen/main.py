# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/main.ui'
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
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 144, 145, 22))
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.buildDirEdit = QtGui.QLineEdit(Dialog)
        Dialog.buildDirEdit.setGeometry(QtCore.QRect(192, 144, 353, 32))
        Dialog.buildDirEdit.setObjectName(_fromUtf8("buildDirEdit"))
        Dialog.buildDirBrowseButton = QtGui.QPushButton(Dialog)
        Dialog.buildDirBrowseButton.setGeometry(QtCore.QRect(560, 144, 41, 32))
        Dialog.buildDirBrowseButton.setAutoDefault(False)
        Dialog.buildDirBrowseButton.setObjectName(_fromUtf8("buildDirBrowseButton"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 609, 97))
        Dialog.label.setWordWrap(True)
        Dialog.label.setObjectName(_fromUtf8("label"))
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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.label_3.setText(_translate("Dialog", "Build Output:", None))
        Dialog.buildDirBrowseButton.setText(_translate("Dialog", "...", None))
        Dialog.label.setText(_translate("Dialog", "Directory where the package is built.   If a package was previously built there, you will be prompted for an updated version and information", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))

