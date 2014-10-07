# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/source.ui'
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
        Dialog.srcDirEdit = QtGui.QLineEdit(Dialog)
        Dialog.srcDirEdit.setGeometry(QtCore.QRect(192, 160, 353, 32))
        Dialog.srcDirEdit.setObjectName(_fromUtf8("srcDirEdit"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(16, 208, 141, 22))
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.srcDirBrowseButton = QtGui.QPushButton(Dialog)
        Dialog.srcDirBrowseButton.setGeometry(QtCore.QRect(560, 158, 41, 32))
        Dialog.srcDirBrowseButton.setAutoDefault(False)
        Dialog.srcDirBrowseButton.setObjectName(_fromUtf8("srcDirBrowseButton"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 160, 151, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.packageEdit = QtGui.QLineEdit(Dialog)
        Dialog.packageEdit.setGeometry(QtCore.QRect(192, 208, 191, 32))
        Dialog.packageEdit.setObjectName(_fromUtf8("packageEdit"))
        Dialog.label_3 = QtGui.QLabel(Dialog)
        Dialog.label_3.setGeometry(QtCore.QRect(16, 16, 609, 97))
        Dialog.label_3.setWordWrap(True)
        Dialog.label_3.setObjectName(_fromUtf8("label_3"))
        Dialog.cancelButton = QtGui.QPushButton(Dialog)
        Dialog.cancelButton.setGeometry(QtCore.QRect(512, 336, 119, 32))
        Dialog.cancelButton.setAutoDefault(False)
        Dialog.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dialog.nextButton = QtGui.QPushButton(Dialog)
        Dialog.nextButton.setGeometry(QtCore.QRect(512, 432, 119, 32))
        Dialog.nextButton.setObjectName(_fromUtf8("nextButton"))
        Dialog.prevButton = QtGui.QPushButton(Dialog)
        Dialog.prevButton.setGeometry(QtCore.QRect(512, 384, 119, 32))
        Dialog.prevButton.setAutoDefault(False)
        Dialog.prevButton.setObjectName(_fromUtf8("prevButton"))
        Dialog.mainScriptEdit = QtGui.QLineEdit(Dialog)
        Dialog.mainScriptEdit.setGeometry(QtCore.QRect(192, 256, 353, 32))
        Dialog.mainScriptEdit.setObjectName(_fromUtf8("mainScriptEdit"))
        Dialog.mainScriptBrowseButton = QtGui.QPushButton(Dialog)
        Dialog.mainScriptBrowseButton.setGeometry(QtCore.QRect(560, 256, 41, 32))
        Dialog.mainScriptBrowseButton.setAutoDefault(False)
        Dialog.mainScriptBrowseButton.setObjectName(_fromUtf8("mainScriptBrowseButton"))
        Dialog.label_4 = QtGui.QLabel(Dialog)
        Dialog.label_4.setGeometry(QtCore.QRect(16, 256, 145, 22))
        Dialog.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.label_2.setText(_translate("Dialog", "Package Name:", None))
        Dialog.srcDirBrowseButton.setText(_translate("Dialog", "...", None))
        Dialog.label.setText(_translate("Dialog", "Source Directory:", None))
        Dialog.label_3.setText(_translate("Dialog", "Root directory where the application scripts and data is.  All files except the ignore list (next step) will be picked up.   The main script should contain the file name that should run your program.", None))
        Dialog.cancelButton.setText(_translate("Dialog", "Cancel", None))
        Dialog.nextButton.setText(_translate("Dialog", "Next", None))
        Dialog.prevButton.setText(_translate("Dialog", "Previous", None))
        Dialog.mainScriptBrowseButton.setText(_translate("Dialog", "...", None))
        Dialog.label_4.setText(_translate("Dialog", "Main Script:", None))

