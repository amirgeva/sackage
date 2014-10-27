from PyQt4 import QtCore,QtGui
import os
import uis
import time
import subprocess as sp

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

def chlogTimestamp():
    return time.strftime('%a, %d %b %Y %H:%M:%S %z')

def getCodename():
    out=sp.check_output(['lsb_release','-a']).split('\n')
    for line in out:
        if line.startswith('Codename:'):
            return (line.split())[-1]
    return ''
    
class GenerateError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

allPackages=[] 

def loadPackageList():
    all=sp.check_output(['dpkg','-l'])
    for line in all.split('\n'):
        parts=line.split()
        if len(parts)>2 and parts[0]=='ii':
            allPackages.append(parts[1])

def allsubs(subs,text):
    for s in subs:
        if not s in text:
            return False
    return True
    
class AddDependDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(AddDependDialog,self).__init__(parent)
        if len(allPackages)==0:
            loadPackageList()
        uis.loadDialog('adddep',self)
        self.filterEdit.textChanged.connect(self.filterChanged)
        self.filterEdit.setFocus(QtCore.Qt.OtherFocusReason)
        self.pkgList.addItems(allPackages)
        self.pkgList.itemSelectionChanged.connect(self.selChanged)
        self.selection=[]
        
    def filterChanged(self,text):
        self.pkgList.clear()
        parts=text.split()
        cur=[p for p in allPackages if allsubs(parts,p)]
        self.pkgList.addItems(cur)
        
    def selChanged(self):
        items=self.pkgList.selectedItems()
        self.selection = [item.text() for item in items]
        
 
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
        print "Trying to setup settings at: '{}'".format(path)
        s=QtCore.QSettings(path)
        print "Loading package settings from: {}".format(s.fileName())
        return s
        
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
    
class UploadDialog(WizardDialog):    
    def __init__(self,props,parent=None):
        super(UploadDialog,self).__init__('upload',props,parent)
        self.userEdit.setText(load('lpuser').toString())
        self.ppaEdit.setText(load('lpppa').toString())
        self.package=self.query('package')
        self.verDir=self.props['verDir']
        self.uploadButton.clicked.connect(self.upload)
        
    def upload(self):
        user=self.userEdit.text()
        ppa=self.ppaEdit.text()
        store('lpuser',user)
        store('lpppa',ppa)
        cmdlist=['dput','ppa:{}/{}'.format(user,ppa)]
        files=os.listdir(self.verDir)
        files=[f for f in files if f.endswith('_source.changes')]
        if len(files)==1:
            cmdlist.append(files[0])
            out=sp.check_output(cmdlist,cwd=self.verDir)
            self.outputEdit.setPlainText(out)
        else:
            QtGui.QMessageBox.warning(self,"Error","Failed to find *_source.changes")
    
##############################################################
    
class GenerateDialog(WizardDialog):
    def __init__(self,props,parent=None):
        super(GenerateDialog,self).__init__('generate',props,parent)
        self.generateButton.clicked.connect(self.generate)

        self.package=self.props['package']
        self.name=self.props['name']
        self.email=self.props['email']
        self.pubKey=self.props['pubKey']
        self.proot=os.path.join(self.props['buildRoot'],self.package)
        s=QtCore.QSettings(os.path.join(self.proot,'settings.ini'))
        self.ver=s.value('ver').toString()
        self.verComment=s.value('verComment').toString()
        self.urgency=s.value('urgency').toString()
        self.license=s.value('license').toString()
        self.section=s.value('section').toString()
        self.priority=s.value('priority').toString()
        self.shortDesc=s.value('shortDesc').toString()
        self.longDesc=s.value('longDesc').toString()
        self.deps=s.value('deps').toString().replace(',',', ')
        self.ignore=s.value('ignore').toString().split(',')
        self.mainScript=s.value('mainScript').toString()
        self.srcDir=s.value('srcDir').toString()
        
        self.verName="{}-{}".format(self.package,self.ver)
        self.verDir=os.path.join(self.proot,self.verName)
        self.props['verDir']=self.verDir
        self.dataDir=os.path.join(self.verDir,self.package)
        self.debDir=os.path.join(self.dataDir,'debian')
        
    def accept(self):
        self.setNextDialog(UploadDialog(self.props))
        
    def generate(self):
        try:
            self.createVerDir()
            if not os.path.exists(self.debDir):
                os.makedirs(self.debDir)
            self.generateTar()
            self.generateMakefile()
            self.generateChangelog()
            self.generateControl()
            self.generateCopyright()
            self.generateRules()
            
            self.buildPackage()
        except GenerateError as e:
            QtGui.QMessageBox.warning(self,"Aborting",e.value)
        
    def buildPackage(self):
        cmdlist=['debuild','-S']
        if len(self.pubKey)>0:
            cmdlist.append('-rfakeroot')
            cmdlist.append('-k{}'.format(self.pubKey))
        texts=['Building Source Package','=========================================']
        out=sp.check_output(cmdlist,cwd=self.dataDir)
        texts.append(out)
        texts.append('\n\n\n')
        texts.append('Building Binary Package')
        texts.append('=========================================')
        cmdlist[1]='-b'
        out=sp.check_output(cmdlist,cwd=self.dataDir)
        texts.append(out)
        self.outputEdit.setPlainText('\n'.join(texts))
        
    def generateRules(self):
        try:
            out=os.path.join(self.debDir,'rules')
            f=open(out,'w')
            f.write("#!/usr/bin/make -f\n%:\n\tdh $@\n")
            f.close()
        except OSError as e:
            raise GenerateError(str(e))
        
        
    def generateCopyright(self):
        try:
            year=time.strftime('%Y')
            out=os.path.join(self.debDir,'copyright')
            f=open(out,'w')
            f.write("Files: *\nCopyright: {} {}".format(year,self.name))
            f.write("License: {}\n\n".format(self.license))
            f.close()
        except OSError as e:
            raise GenerateError(str(e))

    def generateControl(self):
        try:
            out=os.path.join(self.debDir,'control')
            f=open(out,'w')
            f.write("Source: {}\n".format(self.package))
            f.write("Maintainer: {} <{}>\n".format(self.name,self.email))
            f.write("Section: {}\n".format(self.section))
            f.write("Priority: {}\n".format(self.priority))
            f.write("Build-Depends: debhelper (>= 9)\n")
            f.write("\n")
            f.write("Package: {}\n".format(self.package))
            f.write("Architecture: all\n")
            f.write("Depends: {}\n".format(self.deps))
            f.write("Description: {}\n".format(self.shortDesc))
            for line in self.longDesc.split('\n'):
                f.write(' {}\n'.format(line))
            f.close()
        except OSError as e:
            raise GenerateError(str(e))

    def generateChangelog(self):
        prev=''
        if 'lastVer' in self.props:
            prevChangelog=os.path.join(self.props.get('lastVer'),self.props.get('package'),'debian','changelog')
            if os.path.exists(prevChangelog):
                f=open(prevChangelog,'r')
                prev=f.read()
                f.close()
        out=os.path.join(self.debDir,'changelog')
        osver=getCodename()
        try:
            f=open(out,'w')
            f.write('{} ({}) {}; urgency={}\n\n'.format(self.package,self.ver,osver,self.urgency))
            lines=self.verComment.split('\n')
            for line in lines:
                f.write('  * {}\n'.format(line))
            f.write('\n -- {} <{}>  {}\n\n'.format(self.name,self.email,chlogTimestamp()))
            f.write(prev)
            f.close()
        except OSError as e:
            raise GenerateError(str(e))

    def createVerDir(self):
        try:
            if os.path.exists(self.verDir):
                yes=QtGui.QMessageBox.Yes
                yesno=yes | QtGui.QMessageBox.No
                res=QtGui.QMessageBox.question(self,"Packge Directory Exists","Do you want to overwrite?",yesno,yes)
                if res!=yes:
                    raise GenerateError("Aborted")
            else:
                os.mkdir(self.verDir)
        except OSError as e:
            raise GenerateError(str(e))
            
    def generateMakefile(self):
        out=os.path.join(self.dataDir,'Makefile')
        try:
            f=open(out,'w')
            f.write("ifeq ($(DESTDIR),)\n")
            f.write("	DESTDIR=/usr\n")
            f.write("endif\n")
            f.write("\n")
            f.write("all:\n")
            f.write("	echo '#!/bin/sh' > {}\n".format(self.package))
            f.write("	echo $(DESTDIR)/share/{}/{} >> {}\n".format(self.package,self.mainScript,self.package))
            f.write("	chmod +x {}\n".format(self.package))
            f.write("\n")
            f.write("install:\n")
            f.write("	install -d $(DESTDIR)/usr/share/{}\n".format(self.package))
            f.write("	tar -xf data.tar -C $(DESTDIR)/usr/share/{}\n".format(self.package))
            f.write("	install -d $(DESTDIR)/usr/bin\n")
            f.write("	install -t $(DESTDIR)/usr/bin {}\n".format(self.package))
            f.write("\n")
            f.close()
        except OSError as e:
            raise GenerateError(str(e))
            
    def generateTar(self):
        out=os.path.join(self.dataDir,'data.tar')
        cmdlist=['tar','cf',out,'.']
        for pattern in self.ignore:
            cmdlist.append('--exclude='+pattern)
        res=sp.call(cmdlist,cwd=self.srcDir)
        if res!=0:
            raise GenerateError('tar failed with return code {}'.format(res))
        

##############################################################
    
class VersionInfoDialog(WizardDialog):    
    def __init__(self,props,parent=None):
        super(VersionInfoDialog,self).__init__('pkginfo2',props,parent)
        self.lastVersionEdit.setText(self.query('lastVersion'))
        index=self.licenseCB.findText(self.query('license'))
        if index>=0:
            self.licenseCB.setCurrentIndex(index)
        index=self.urgencyCB.findText(self.query('urgency'))
        if index>=0:
            self.urgencyCB.setCurrentIndex(index)
        self.versionCommentEdit.setPlainText(self.query('verComment'))
    
    def accept(self):
        ver=self.newVersionEdit.text()
        urgency=self.urgencyCB.currentText()
        license=self.licenseCB.currentText()
        comment=self.versionCommentEdit.toPlainText()
        if ver and comment:
            self.assign('ver',ver)
            self.assign('urgency',urgency)
            self.assign('license',license)
            self.assign('verComment',comment)
            self.setNextDialog(GenerateDialog(self.props))
        else:
            QtGui.QMessageBox.warning(self,"Error","Cannot continue without all fields")
    
##############################################################
    
class PackageInfoDialog(WizardDialog):    
    def __init__(self,props,parent=None):
        super(PackageInfoDialog,self).__init__('pkginfo',props,parent)
        self.addButton.clicked.connect(self.addDep)
        self.removeButton.clicked.connect(self.removeDep)
        from sections import Sections
        sortedSections=sorted(Sections.items(),key=lambda x : x[1])
        self.sortedSectionCodes=[x[0] for x in sortedSections]
        sortedSectionNames=[x[1] for x in sortedSections]
        self.sectionCB.addItems(sortedSectionNames)
        sel=self.query('section')
        try:
            index=self.sortedSectionCodes.index(sel)
            self.sectionCB.setCurrentIndex(index)
        except ValueError:
            pass
        index=self.priorityCB.findText(self.query('priority'))
        if index>=0:
            self.priorityCB.setCurrentIndex(index)
        self.shortDescEdit.setText(self.query('shortDesc'))
        self.longDescEdit.setPlainText(self.query('longDesc'))
        deps=self.query('deps').split(',')
        deps=[d for d in deps if d]
        if len(deps)>0:
            self.dependList.addItems(deps)
        
    def accept(self):
        index=self.sectionCB.currentIndex()
        section=self.sortedSectionCodes[index]
        self.assign('section',section)
        self.assign('priority',self.priorityCB.currentText())
        self.assign('shortDesc',self.shortDescEdit.text())
        self.assign('longDesc',self.longDescEdit.toPlainText())
        ndeps=self.dependList.count()
        deps=[]
        for i in xrange(0,ndeps):
            deps.append(self.dependList.item(i).text())
        self.assign('deps',','.join(deps))
        self.setNextDialog(VersionInfoDialog(self.props))
        
    def removeDep(self):
        sel=self.dependList.selectedItems()
        for item in sel:
            self.dependList.removeItemWidget(item)
            
    def addDep(self):
        d=AddDependDialog()
        if d.exec_():
            for s in d.selection:
                self.dependList.addItem(s)
    
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
            res.append(self.ignoreList.item(i).text())
        self.assign('ignore',','.join(res))
        self.setNextDialog(PackageInfoDialog(self.props))
            
            
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
            pkgDir=os.path.join(self.dir,package)
            verDirs=os.listdir(pkgDir)
            verDirs=sorted(verDirs)
            lastVer=os.path.join(pkgDir,verDirs[-1])
            lastVerNum=(lastVer.split('-'))[-1]
            self.props['lastVer']=lastVer
            path=os.path.join(pkgDir,'settings.ini')
            s=QtCore.QSettings(path)
            s.setValue('lastVersion',lastVerNum)
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
        self.pubKeyEdit.setText(load('pubKey').toString())
        
    def accept(self):
        name=self.nameEdit.text()
        email=self.emailEdit.text()
        pubKey=self.pubKeyEdit.text()
        if name and email:
            self.props['name']=name
            self.props['email']=email
            self.props['pubKey']=pubKey
            store('pubKey',pubKey)
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
            
    