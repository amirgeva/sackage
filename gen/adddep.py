# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/adddep.ui'
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
        Dialog.resize(413, 414)
        Dialog.buttonBox = QtGui.QDialogButtonBox(Dialog)
        Dialog.buttonBox.setGeometry(QtCore.QRect(-16, 368, 417, 32))
        Dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        Dialog.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        Dialog.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        Dialog.filterEdit = QtGui.QLineEdit(Dialog)
        Dialog.filterEdit.setGeometry(QtCore.QRect(128, 16, 273, 32))
        Dialog.filterEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        Dialog.filterEdit.setObjectName(_fromUtf8("filterEdit"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.pkgList = QtGui.QListWidget(Dialog)
        Dialog.pkgList.setGeometry(QtCore.QRect(16, 64, 385, 289))
        Dialog.pkgList.setObjectName(_fromUtf8("pkgList"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(Dialog.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(Dialog.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Dependency", None))
        Dialog.label.setText(_translate("Dialog", "Filter:", None))

