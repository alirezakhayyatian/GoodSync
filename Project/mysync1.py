import os
import sys
#from waitingspinnerwidget import QtWaitingSpinner
from PyQt5 import uic, QtGui,QtCore,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QFileDialog,QProgressBar,QAction,QGridLayout,QLabel,QFrame, QDialog, QHBoxLayout,QFileSystemModel,QTreeView,QListView
from PyQt5.QtCore import QThread
import random
import shutil
import time as timer1
import sqlite3
from typing import Any
from time import  time as epochTime
from pathlib import Path
import threading

Form = uic.loadUiType(os.path.join(os.getcwd(), 'MySync.ui'))[0]
Form2 = uic.loadUiType(os.path.join(os.getcwd(), 'NewJob.ui'))[0]

class NewJobWindow(Form2, QMainWindow):
    def __init__(self):
        
        Form2.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setStyleSheet("{background-image: url(bgnd.jpg)}")
        self.setFixedSize(550,400)        
        self.pushButton.clicked.connect(self.ok_button)
    def ok_button(self):
        global JobName
        JobName= self.lineEdit.text()
        if not self.JobName == "":
            self.close()
class IntroWindow(Form, QMainWindow):
    '''
        main window of the program !!!
    '''
    def __init__(self):
       '''
            constructor
       '''
       Form.__init__(self)
       QMainWindow.__init__(self)
       self.setupUi(self)
       grid_layout = QGridLayout(self)
       self.setLayout(grid_layout)
       new_JobCreated=0
       self.right_directory_address = str("jkjkbjkbkj")
       self.left_directory_address = str("klnjkkjkjnnjknjnnnnnnnn")
       self.label.setScaledContents(True)
       self.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/2 (2).svg"))
       self.thread = ThreadClass()
       self.thread.signal.connect(self.onfinished)

       self.thread2 = ThreadClass2()
       self.thread2.signal.connect(self.onfinished2)

       self.btn_newJob = QtWidgets.QToolButton(self)
       self.btn_newJob.setIcon(QtGui.QIcon('add.svg'))
       self.btn_newJob.setIconSize(QSize(56, 56))
       self.btn_newJob.setStyleSheet("border: none; textformat: ToolButtonTextUnderIcon; text: 'analyze';")
       self.btn_newJob.setToolTip("New Job")
       self.btn_newJob.clicked.connect(self.New_Job_func)
       
       self.btn_newGroup = QtWidgets.QToolButton(self)
       self.btn_newGroup.setIcon(QtGui.QIcon('list.svg'))
       self.btn_newGroup.setIconSize(QSize(56, 56))
       self.btn_newGroup.setStyleSheet("border: none; textformat: ToolButtonTextUnderIcon; text: 'analyze';")
       self.btn_newGroup.setToolTip("New Group")
       self.horizontalLayout_3.addWidget(self.btn_newJob)
       self.horizontalLayout_3.addWidget(self.btn_newGroup)

       self.btn_autoRun = QtWidgets.QToolButton(self)
       self.btn_autoRun.setIcon(QtGui.QIcon('auto-flash.svg'))
       self.btn_autoRun.setIconSize(QSize(56, 56))
       self.btn_autoRun.setStyleSheet("border: none; textformat: ToolButtonTextUnderIcon; text: 'analyze';")
       self.btn_autoRun.setToolTip("Auto Run")
       self.horizontalLayout_3.addWidget(self.btn_autoRun)
    
       self.btn_analyse = QtWidgets.QToolButton(self)
       self.btn_analyse.setIcon(QtGui.QIcon('search.svg'))
       self.btn_analyse.setIconSize(QSize(56, 56))
       self.btn_analyse.setStyleSheet("border: none; textformat: ToolButtonTextUnderIcon; text: 'analyze';")
       self.btn_analyse.setToolTip("Analyse")
       self.btn_analyse.setEnabled(False)
       self.btn_analyse.clicked.connect(self.analyze)
       self.horizontalLayout_2.addWidget(self.btn_analyse)
       
       self.btn_sync = QtWidgets.QToolButton(self)
       self.btn_sync.setIcon(QtGui.QIcon('sync2.svg'))
       self.btn_sync.setIconSize(QSize(56, 56))
       self.btn_sync.setStyleSheet("border: none; textformat: ToolButtonTextUnderIcon; text: 'analyze';")
       self.btn_sync.setToolTip("Sync")
       self.btn_sync.setEnabled(False)
       self.btn_sync.clicked.connect(self.sync)
       self.horizontalLayout_2.addWidget(self.btn_sync)
       
       self.btn_leftDir=QPushButton(self)       
       self.btn_leftDir.setIcon(QtGui.QIcon('folder.svg'))
       self.btn_leftDir.setIconSize(QSize(56,56))
       self.btn_leftDir.setLayoutDirection(Qt.RightToLeft)
       self.btn_leftDir.clicked.connect(self.show_folder_left)
       self.horizontalLayout.addWidget(self.btn_leftDir)
       
       self.btn_change=QPushButton(self)
       self.btn_change.setStyleSheet("border: none")
       self.btn_change.setIcon(QtGui.QIcon('exchange-arrows.svg'))
       self.btn_change.setIconSize(QSize(56,56))
       self.horizontalLayout.addWidget(self.btn_change)
       
       self.btn_rightDir=QPushButton(self)
       self.btn_rightDir.setIcon(QtGui.QIcon('folder.svg'))
       self.btn_rightDir.setIconSize(QSize(56,56))
       self.btn_rightDir.clicked.connect(self.show_folder_right)
       self.horizontalLayout.addWidget(self.btn_rightDir)

       self.label.setStyleSheet("border: 1px solid grey")
       #self.btn_rightDir.setEnabled(False)
       #self.btn_leftDir.setEnabled(False)
       #self.btn_change.setEnabled(False)
       self.a = NewJobWindow()
       self.setFocusPolicy(Qt.StrongFocus)
# =============================================================================
#        self.Label = QLabel(self)
#        self.Label.setText("first line\nsecond line")
#        self.Label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
#        self.Label.setFixedWidth(300)
#        self.Label.setParent(self.frame)
#        
# =============================================================================
# =============================================================================
#       
#        self.Label2 = QLabel(self)
#        self.Label2.setText("first line\nsecond line")
#        self.Label2.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
#        self.Label2.setFixedWidth(50)
#        self.Label2.setParent(self.frame_2)
# =============================================================================
       #self.frame_2=QFrame()
# =============================================================================
#         self.dialog.pushButton.clicked.connect(self.dialog.ok_button,self.Ok)
# =============================================================================
    def focusInEvent(self, event):
        #self.label.setText('Got focus')
        print('^^^^^^^')
    def New_Job_func(self):
        self.a.show()

    def sync(self):
        '''
            A FUNCTION TO SYNCING TWO SELECTED FOLDER
        '''
        self.label_finish.hide()
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 0)
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.thread2.start()  # starts spinning

    def analyze(self):
        '''
            THIS FUNCTION FIND THE FILES AND FOLDER THAT THEY ARE DIFFERENT IN TWO SELECTED FOLDER
        '''
        self.label.hide()
        self.DataBase()


    def onfinished(self):
        '''
            FUNCTION OF FINISHING THE THREAD !!!
        '''
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)
        timer1.sleep(1)
        self.progressBar.hide()
        self.label_finish = QLabel()
        self.label_finish.setStyleSheet("QLabel {color : green}")
        self.label_finish.setFont(QtGui.QFont('Helvetica', 15,QtGui.QFont.DemiBold))
        self.label_finish.setText("DB Created !!")
        self.horizontalLayout_8.addWidget(self.label_finish)
        self.btn_sync.setEnabled(True)

    def onfinished2(self):
        '''
        FUNCTION OF FINISHING THE THREAD !!!
        '''
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)
        timer1.sleep(1)
        self.progressBar.hide()
        self.label_finish = QLabel()
        self.label_finish.setStyleSheet("QLabel {color : green}")
        self.label_finish.setFont(QtGui.QFont('Helvetica', 15,QtGui.QFont.DemiBold))
        self.label_finish.setText("Synced !!")
        self.horizontalLayout_8.addWidget(self.label_finish)

    def Ok(self):
        self.label_2.setText(str(self.dialog.JobName))
        self.btn_sync.setEnabled(True)
        self.btn_leftDir.setEnabled(True)
        self.btn_rightDir.setEnabled(True)
        
    def show_folder_left(self):
        '''
            FUNCTION TO SHOW ALL YOUR COMPUTER FOLDER FOR LEFT DIRECTORY
        '''
        dialog=QFileDialog(self)
        global file_test
        file_test=str(dialog.getExistingDirectory(self,"Select Directory"))
        self.btn_leftDir.setText(file_test)
        if file_test and self.btn_rightDir.text():
            self.btn_analyse.setEnabled(True)

        
        self.left_directory_address =  self.btn_leftDir.text()
        
    def show_folder_right(self):
        '''
            FUNCTION TO SHOW ALL YOUR COMPUTER FOLDER FOR RIGHT DIRECTORY
        '''
        dialog=QFileDialog(self)
        global file_test2
        file_test2=str(dialog.getExistingDirectory(self,"Select Directory"))
        self.btn_rightDir.setText(file_test2)
        self.right_directory_address = self.btn_rightDir.text()
        if file_test2 and self.btn_leftDir.text():
            self.btn_analyse.setEnabled(True)

    def Draw_Left_Dir(self):
        '''
            FUNCTION TO SHOW LEFT DIRECTORY
        '''
        self.left_directory_address =  self.btn_leftDir.text()
        self.model = QFileSystemModel()
        self.model.setRootPath(str(QDir(self.btn_leftDir.text())))
        print(self.model.rootPath())
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.btn_leftDir.text()))
        self.tree.setStyleSheet("background-color: rgb(69, 170,0)")
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.horizontalLayout_5.addWidget(self.tree)
        
        
    def Draw_Right_Dir(self):
        '''
            FUNCTION TO SHOW RIGHT DIRECTORY
        '''
        self.left_directory_address = self.btn_leftDir.text()
        self.model = QFileSystemModel()
        self.model.setRootPath(str(QDir(self.btn_leftDir.text())))
        print(self.model.rootPath())
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.btn_rightDir.text()))
        self.tree.setStyleSheet("background-color: rgb(69, 170, 204)")
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.horizontalLayout_5.addWidget(self.tree)
        
    def DataBase(self):
        '''
            A FUNCTION THAT START THE THREAD OF THE DATA_BASE
        '''
        self.Draw_Left_Dir()
        self.Draw_Right_Dir()
        self.progressBar = QProgressBar()
        self.progressBar.setFormat('Creating DataBase...')
        self.progressBar.setStyleSheet("text-align: center;")
        self.progressBar.setRange(0, 0)
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.thread.start()  # starts spinning
 




class ThreadClass(QtCore.QThread):
    signal = pyqtSignal()
    def __init__(self):
        QtCore.QThread.__init__(self)
    def run(self):
        DB(file_test,file_test2)
        #alireza.createDB
        self.signal.emit()


class ThreadClass2(QtCore.QThread):
    signal = pyqtSignal()

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        for i in range(10000):
            for j in range(10000):
                pass
        # alireza.createDB
        self.signal.emit()

def DB(g1,g2):
    start = epochTime()
    connection = sqlite3.connect(os.path.join(os.getcwd(), 'gdb.db'))
    mycursor = connection.cursor()

    #############function to encode & decode############
    def encode(a):
        a = a.replace("\\", "$")
        a = a.replace("/", "$")
        a = a.replace(":", "___")
        # print(a)
        return a

    def decode(a):
        a = a.replace("$", "\\")
        a = a.replace("___", ":")
        # print(a)
        return a

    #############function to encode & decode############
    mycursor.execute(" CREATE TABLE IF NOT EXISTS previous_dir (id integer primary key AUTOINCREMENT ,dir VARCHAR(255),"
                     "lastCheck timestamp) ")

    input_right = g1
    input_left = g2
    right = encode(input_right)
    left = encode(input_left)
    for i in range(2):

        stmt = "select id  from previous_dir where dir=?"
        args = (encode(input_right),)

        mycursor.execute(stmt, args)
        input_exists = mycursor.fetchall()
        zz = "{}".format(encode(input_right))
        if (len(input_exists)) == 0:
            sql = "insert into previous_dir (dir,lastcheck) values (?,?)"
            val = (encode(input_right), epochTime())
            mycursor.execute(sql, val)
            connection.commit()

            # hg=input_exists[1][0]
            # print(decode(encode(input_right)))

            # zz="{}".format(encode(input_right))
            mycursor.execute(" CREATE TABLE IF NOT EXISTS {}(id  AUTO_INCREMENT ,name VARCHAR(255)"
                             ",path VARCHAR(255),rank integer ,created timestamp ,modified timestamp ,"
                             "size_file float ,flag integer ,copied integer,isFolder integer )".format(zz))

            for root, dirs, files in os.walk(input_right):
                # print(root)
                # print(files)
                sql = "INSERT INTO {}(name,path,rank,created,modified,size_file" \
                      ",flag,copied,isFolder ) VALUES (?,?,?,?,?,?,?,?,?)".format(zz)
                cc = root[len(input_right):]
                dd = str(cc.count("\\"))

                os.chdir(root)
                val = [(root, 0, dd, os.path.getctime(root), 0, 0, 0, 0, 1)]
                # print(val)
                mycursor.executemany(sql, val)
                connection.commit()

                for x in files:
                    # print (root)
                    cc = root[len(input_right):]
                    # print(x)
                    # print(cc)
                    dd = str(cc.count("\\"))
                    # print(dd)
                    # os.chdir(root)
                    val = [(x, cc, dd, os.path.getctime(x), os.path.getmtime(x), os.path.getsize(x), 0, 0, 0)]
                    # print(val)
                    mycursor.executemany(sql, val)
                    connection.commit()

        ##########################################3fdgsfdgmh############################

        if (len(input_exists)) != 0:

            stmt = "select lastcheck,id  from previous_dir where dir=?"
            args = (encode(input_right),)
            mycursor.execute(stmt, args)
            input_exists = mycursor.fetchall()
            # print(input_exists)
            # print(len(input_exists))
            # print(input_exists[-1])
            timer = input_exists[-1][0]

            sql = "UPDATE  previous_dir SET lastcheck=? WHERE dir=?"

            val = (epochTime(), encode(input_right))
            mycursor.execute(sql, val)
            connection.commit()
            print("dddd")

            for root, dirs, files in os.walk(input_right):

                sql = "INSERT INTO {}(name,path,rank,created,modified,size_file" \
                      ",flag,copied,isFolder ) VALUES (?,?,?,?,?,?,?,?,?)".format(zz)
                cc = root[len(input_right):]
                dd = str(cc.count("\\"))

                os.chdir(root)
                ctime = os.path.getctime(root)

                # print(val)
                if timer < ctime:
                    val = [(root, 0, dd, ctime, 0, 0, 0, 0, 1)]
                    mycursor.executemany(sql, val)
                    connection.commit()

                for x in files:
                    # os.chdir(root)
                    ctime = os.path.getctime(x)
                    mtime = os.path.getmtime(x)
                    if timer < ctime or timer < mtime:
                        # sql = "INSERT INTO {}(name,path,rank,created,modified,size_file" \
                        #                                 ",flag,copied,isFolder) VALUES (?,?,?,?,?,?,?,?,?)".format(zz)
                        cc = root[len(input_right):]
                        dd = str(cc.count("\\"))
                        # print(dd)
                        val = [(x, cc, dd, ctime, mtime, os.path.getsize(x), 1, 1, 0)]
                        mycursor.executemany(sql, val)
                        connection.commit()

        # print(input_right)
        input_right = input_left
        # print(input_right)

    #####################End of generate table#################################
    print("end task")
    print(epochTime() - start)

def changedFocusSlot(old, now):
    if (now==None and QApplication.activeWindow()!=None):
        print ("set focus to the active window")
        QApplication.activeWindow().setFocus()


app = QApplication(sys.argv)
QObject.connect(app, SIGNAL("focusChanged(QWidget *, QWidget *)"), changedFocusSlot)
app.setStyle('plastique')
w =IntroWindow()
w.setWindowTitle("MySync")
w.setWindowIcon(QtGui.QIcon('sync.svg'))

w.show()
sys.exit(app.exec())
