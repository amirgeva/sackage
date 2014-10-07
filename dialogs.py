from PyQt4 import QtCore,QtGui
import os
import uis

def getenv(key,default):
    if key in os.environ:
        return os.environ.get(key)
    return default

def store(name,value):
    QtCore.QSettings().setValue(name,value)

def load(name,default=''):
    return QtCore.QSettings().value(name,default)

def get(props,name,default=''):
    if name in props:
        return props.get(name)
    return default

class WizardDialog(QtGui.QDialog):
    def __init__(self,dlgName,props,parent=None):
        super(WizardDialog,self).__init__(parent)
        self.nextDialog=None
        self.props=props
        uis.loadDialog(dlgName,self)
        self.cancelButton.clicked.connect(self.reject)
        self.nextButton.clicked.connect(self.accept)
        self.settings=None
    
    def getNextDialog(self):
        return self.nextDialog
        
    def setNextDialog(self,d):
        self.nextDialog=d
        super(WizardDialog,self).accept()
        
    def buildRoot(self):
        return self.props['buildRoot']
        
    def packageRoot(self):
        return os.path.join(self.buildRoot(),self.props['package'])
        
    def packageSettings(self):
        path=os.path.join(self.packageRoot(),'settings.ini')
        return QtCore.QSettings(path)
        
    def query(self,name,default=''):
        if not self.settings:
            self.settings=self.packageSettings()
        return self.settings.value(name,default).toString()
        
    def assign(self,name,value):
        if not self.settings:
            self.settings=self.packageSettings()
        self.settings.setValue(name,value)
        self.settings.sync()
    
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################

class IgnoreDialog(WizardDialog):    
    def __init__(self,props,parent=None):
        super(IgnoreDialog,self).__init__('ignore',props,parent)
        self.ignoreList.clear()
        patterns=self.query('ignore').split(',')
        patterns=[p for p in patterns if p]
        if len(patterns)>0:
            self.ignoreList.addItems(patterns)
        self.addButton.clicked.connect(self.add)
        self.removeButton.clicked.connect(self.remove)
        
    def add(self):
        (text,ok)=QtGui.QInputDialog.getText(self,"Ignore Pattern","Enter ignore pattern")
        if ok:
            self.ignoreList.addItem(text)
            
    def remove(self):
        sel=self.ignoreList.selectedItems()
        for item in sel:
            self.ignoreList.removeItemWidget(item)
            
    def accept(self):
        n=self.ignoreList.count()
        res=[]
        for i in xrange(0,n):
            res.append(self.ignoreList.itemFromIndex(i).text())
        self.assign('ignore',','.join(res))
        self.setNextDialog()
            
            
##############################################################

class SourceDialog(WizardDialog):
    def __init__(self,props,parent=None):
        super(SourceDialog,self).__init__('source',props,parent)
        self.srcDirEdit.setText(get(props,'srcDir'))
        self.packageEdit.setText(get(props,'package'))
        self.mainScriptEdit.setText(get(props,'mainScript'))
        self.srcDirBrowseButton.clicked.connect(self.srcBrowse)
        self.mainScriptBrowseButton.clicked.connect(self.mainBrowse)
        
    def srcBrowse(self):
        path=self.srcDirEdit.text()
        path=QtGui.QFileDialog.getExistingDirectory(directory=path)
        if path:
            self.srcDirEdit.setText(path)
            
    def mainBrowse(self):
        dir=self.srcDirEdit.text()
        path=QtGui.QFileDialog.getOpenFileName(directory=dir)
        if path and os.path.exists(path) and not os.path.isdir(path):
            name=os.path.basename(path)
            self.mainScriptEdit.setText(name)
        else:
            QtGui.QMessageBox.warning(self,'Error','Must select existing file')
        
    def accept(self):
        srcDir=self.srcDirEdit.text()
        mainScript=self.mainScriptEdit.text()
        package=self.packageEdit.text()
        if srcDir and mainScript and package:
            self.props['package']=package
            self.props['mainScript']=mainScript
            self.props['srcDir']=srcDir
            root=self.packageRoot()
            if not os.path.exists(root):
                os.mkdir(root)
            self.assign('mainScript',mainScript)
            self.assign('srcDir',srcDir)
            self.setNextDialog(IgnoreDialog(self.props))
        else:
            QtGui.QMessageBox.warning(self,"Error","Cannot proceed without all fields")
            
##############################################################

class ExistingDialog(WizardDialog):            
    def __init__(self,props,parent=None):
        super(ExistingDialog,self).__init__('existing',props,parent)
        self.dir=self.buildRoot()
        self.names=os.listdir(self.dir)
        self.names=[os.path.join(self.dir,n) for n in self.names]
        self.names=[n for n in self.names if os.path.isdir(n)]
        self.names=[os.path.basename(n) for n in self.names]
        self.packageList.addItems(self.names)
        
    def accept(self):
        sel=self.packageList.selectedItems()
        if len(sel)>1:
            QtGui.QMessageBox.warning(self,"Error","Only one package can be selected")
        elif len(sel)==0:
            self.setNextDialog(SourceDialog(self.props))
        else:
            package=sel[0].text()
            self.props['package']=package
            path=os.path.join(self.dir,package,'settings.ini')
            s=QtCore.QSettings(path)
            self.props['mainScript']=s.value('mainScript').toString()
            self.props['srcDir']=s.value('srcDir').toString()
            self.setNextDialog(SourceDialog(self.props))
            
        
##############################################################

class MainDialog(WizardDialog):    
    def __init__(self,props,parent=None):
        super(MainDialog,self).__init__('main',props,parent)
        self.buildDirEdit.setText(load('buildRoot').toString())
        self.buildDirBrowseButton.clicked.connect(self.browse)
        
    def browse(self):
        path=self.buildDirEdit.text()
        path=QtGui.QFileDialog.getExistingDirectory(directory=path)
        if path:
            self.buildDirEdit.setText(path)

    def accept(self):
        path=self.buildDirEdit.text()
        if os.path.exists(path) and os.path.isdir(path):
            self.props['buildRoot']=path
            store('buildRoot',path)
            d=ExistingDialog(self.props)
            if len(d.names)>0:
                self.setNextDialog(d)
            else:
                self.setNextDialog(SourceDialog(self.props))
        else:
            QtGui.QMessageBox.warning(self,'Error','Must select existing directory')
            
##############################################################

class NameDialog(WizardDialog):
    def __init__(self,props,parent=None):
        super(NameDialog,self).__init__('name',props,parent)
        self.bashrcButton.clicked.connect(self.addToBash)
        self.nameEdit.setText(getenv('DEBFULLNAME',''))
        self.emailEdit.setText(getenv('DEBEMAIL',''))
        
    def accept(self):
        name=self.nameEdit.text()
        email=self.emailEdit.text()
        if name and email:
            self.setNextDialog(MainDialog(self.props))
        else:
            QtGui.QMessageBox.warning(self,"Error","Cannot continue without maintainer details")
            
    def addToBash(self):
        name=self.nameEdit.text()
        email=self.emailEdit.text()
        if name and email:
            home=getenv('HOME','')
            if home:
                f=open(os.path.join(home,'.bashrc'),'a')
                f.write('\nexport DEBFULLNAME="{}"\n'.format(name))
                f.write('export DEBEMAIL="{}"\n'.format(email))
                f.close()
            else:
                QtGui.QMessageBox.warning(self,"Error","Home directory not defined")
        else:
            QtGui.QMessageBox.warning(self,"Error","Cannot write partial or empty maintainer details")
            
    