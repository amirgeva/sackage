#!/usr/bin/env python
import sys

try:
    import sip
    sip.setapi('QString', 2)
except ImportError:
    print "sip not installed.  try:   sudo apt-get install python-sip"
    sys.exit(1)

try:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
except ImportError:
    print "PyQt4 not installed.  try:   sudo apt-get install python-qt4"
    sys.exit(1)

def main():
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("MLGSoft")
    QtCore.QCoreApplication.setOrganizationDomain("mlgsoft.com")
    QtCore.QCoreApplication.setApplicationName("Sackage")
    props={}
    from dialogs import NameDialog
    d=NameDialog(props)
    while d:
        if d.exec_():
            d=d.getNextDialog()
        else:
            break

if __name__=='__main__':
    main()

