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
        Dialog.label.setGeometry(QtCore.QRect(16, 176, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.licenseCB = QtGui.QComboBox(Dialog)
        Dialog.licenseCB.setGeometry(QtCore.QRect(160, 176, 241, 32))
        Dialog.licenseCB.setObjectName(_fromUtf8("licenseCB"))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.licenseCB.addItem(_fromUtf8(""))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(16, 32, 129, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.newVersionEdit = QtGui.QLineEdit(Dialog)
        Dialog.newVersionEdit.setGeometry(QtCore.QRect(160, 32, 113, 32))
        Dialog.newVersionEdit.setObjectName(_fromUtf8("newVersionEdit"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 80, 129, 22))
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.lastVersionEdit = QtGui.QLineEdit(Dialog)
        Dialog.lastVersionEdit.setGeometry(QtCore.QRect(160, 80, 113, 32))
        Dialog.lastVersionEdit.setReadOnly(True)
        Dialog.lastVersionEdit.setObjectName(_fromUtf8("lastVersionEdit"))
        Dialog.urgencyCB = QtGui.QComboBox(Dialog)
        Dialog.urgencyCB.setGeometry(QtCore.QRect(160, 128, 145, 32))
        Dialog.urgencyCB.setObjectName(_fromUtf8("urgencyCB"))
        Dialog.urgencyCB.addItem(_fromUtf8(""))
        Dialog.urgencyCB.addItem(_fromUtf8(""))
        Dialog.urgencyCB.addItem(_fromUtf8(""))
        Dialog.urgencyCB.addItem(_fromUtf8(""))
        Dialog.urgencyCB.addItem(_fromUtf8(""))
        Dialog.label_4 = QtGui.QLabel(Dialog)
        Dialog.label_4.setGeometry(QtCore.QRect(16, 128, 84, 22))
        Dialog.label_4.setObjectName(_fromUtf8("label_4"))
        Dialog.label_5 = QtGui.QLabel(Dialog)
        Dialog.label_5.setGeometry(QtCore.QRect(16, 240, 129, 49))
        Dialog.label_5.setWordWrap(True)
        Dialog.label_5.setObjectName(_fromUtf8("label_5"))
        Dialog.versionCommentEdit = QtGui.QPlainTextEdit(Dialog)
        Dialog.versionCommentEdit.setGeometry(QtCore.QRect(160, 240, 305, 225))
        Dialog.versionCommentEdit.setObjectName(_fromUtf8("versionCommentEdit"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 336, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.prevButton = QtGui.QPushButton(Dialog)
        Dialog.prevButton.setGeometry(QtCore.QRect(512, 384, 119, 32))
        Dialog.prevButton.setAutoDefault(False)
        Dialog.prevButton.setObjectName(_fromUtf8("prevButton"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.label_6 = QtGui.QLabel(Dialog)
        Dialog.label_6.setGeometry(QtCore.QRect(288, 32, 321, 22))
        Dialog.label_6.setObjectName(_fromUtf8("label_6"))
        Dialog.label_7 = QtGui.QLabel(Dialog)
        Dialog.label_7.setGeometry(QtCore.QRect(288, 80, 353, 22))
        Dialog.label_7.setObjectName(_fromUtf8("label_7"))
        Dialog.label_8 = QtGui.QLabel(Dialog)
        Dialog.label_8.setGeometry(QtCore.QRect(320, 128, 321, 22))
        Dialog.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Version Information", None))
        Dialog.label.setText(_translate("Dialog", "License:", None))
        Dialog.licenseCB.setItemText(0, _translate("Dialog", "Apache-2.0", None))
        Dialog.licenseCB.setItemText(1, _translate("Dialog", "BSD", None))
        Dialog.licenseCB.setItemText(2, _translate("Dialog", "GFDL-1.2", None))
        Dialog.licenseCB.setItemText(3, _translate("Dialog", "GFDL-1.3", None))
        Dialog.licenseCB.setItemText(4, _translate("Dialog", "GPL-1", None))
        Dialog.licenseCB.setItemText(5, _translate("Dialog", "GPL-2", None))
        Dialog.licenseCB.setItemText(6, _translate("Dialog", "GPL-3", None))
        Dialog.licenseCB.setItemText(7, _translate("Dialog", "LGPL-2", None))
        Dialog.licenseCB.setItemText(8, _translate("Dialog", "LGPL-2.1", None))
        Dialog.licenseCB.setItemText(9, _translate("Dialog", "LGPL-3", None))
        Dialog.label_2.setText(_translate("Dialog", "New Version:", None))
        Dialog.label_3.setText(_translate("Dialog", "Last Version:", None))
        Dialog.urgencyCB.setItemText(0, _translate("Dialog", "low", None))
        Dialog.urgencyCB.setItemText(1, _translate("Dialog", "medium", None))
        Dialog.urgencyCB.setItemText(2, _translate("Dialog", "high", None))
        Dialog.urgencyCB.setItemText(3, _translate("Dialog", "emergency", None))
        Dialog.urgencyCB.setItemText(4, _translate("Dialog", "critical", None))
        Dialog.label_4.setText(_translate("Dialog", "Urgency:", None))
        Dialog.label_5.setText(_translate("Dialog", "New Version Comment:", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.label_6.setText(_translate("Dialog", "Give your package a version number", None))
        Dialog.label_7.setText(_translate("Dialog", "The last version you made, for reference", None))
        Dialog.label_8.setText(_translate("Dialog", "How urgent is this update?", None))

