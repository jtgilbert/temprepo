# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preprocessing.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(742, 489)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_tab1 = QtGui.QLabel(self.tab)
        self.label_tab1.setObjectName(_fromUtf8("label_tab1"))
        self.verticalLayout_2.addWidget(self.label_tab1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labDEM_tab1 = QtGui.QLabel(self.tab)
        self.labDEM_tab1.setObjectName(_fromUtf8("labDEM_tab1"))
        self.verticalLayout_3.addWidget(self.labDEM_tab1)
        self.txtDEM_tab1 = QtGui.QLineEdit(self.tab)
        self.txtDEM_tab1.setObjectName(_fromUtf8("txtDEM_tab1"))
        self.verticalLayout_3.addWidget(self.txtDEM_tab1)
        self.labWats_tab1 = QtGui.QLabel(self.tab)
        self.labWats_tab1.setObjectName(_fromUtf8("labWats_tab1"))
        self.verticalLayout_3.addWidget(self.labWats_tab1)
        self.txtWats_tab1 = QtGui.QLineEdit(self.tab)
        self.txtWats_tab1.setObjectName(_fromUtf8("txtWats_tab1"))
        self.verticalLayout_3.addWidget(self.txtWats_tab1)
        self.labEpsg_tab1 = QtGui.QLabel(self.tab)
        self.labEpsg_tab1.setObjectName(_fromUtf8("labEpsg_tab1"))
        self.verticalLayout_3.addWidget(self.labEpsg_tab1)
        self.txtEpsg_tab1 = QtGui.QLineEdit(self.tab)
        self.txtEpsg_tab1.setObjectName(_fromUtf8("txtEpsg_tab1"))
        self.verticalLayout_3.addWidget(self.txtEpsg_tab1)
        self.labOutput_tab1 = QtGui.QLabel(self.tab)
        self.labOutput_tab1.setObjectName(_fromUtf8("labOutput_tab1"))
        self.verticalLayout_3.addWidget(self.labOutput_tab1)
        self.txtOutput_tab1 = QtGui.QLineEdit(self.tab)
        self.txtOutput_tab1.setObjectName(_fromUtf8("txtOutput_tab1"))
        self.verticalLayout_3.addWidget(self.txtOutput_tab1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.btnDEM_tab1 = QtGui.QPushButton(self.tab)
        self.btnDEM_tab1.setObjectName(_fromUtf8("btnDEM_tab1"))
        self.verticalLayout_5.addWidget(self.btnDEM_tab1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.btnWats_tab1 = QtGui.QPushButton(self.tab)
        self.btnWats_tab1.setObjectName(_fromUtf8("btnWats_tab1"))
        self.verticalLayout_5.addWidget(self.btnWats_tab1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.btnOutput_tab1 = QtGui.QPushButton(self.tab)
        self.btnOutput_tab1.setObjectName(_fromUtf8("btnOutput_tab1"))
        self.verticalLayout_5.addWidget(self.btnOutput_tab1)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.btnOk_tab1 = QtGui.QPushButton(self.tab)
        self.btnOk_tab1.setObjectName(_fromUtf8("btnOk_tab1"))
        self.horizontalLayout_3.addWidget(self.btnOk_tab1)
        self.btnCancel_tab1 = QtGui.QPushButton(self.tab)
        self.btnCancel_tab1.setObjectName(_fromUtf8("btnCancel_tab1"))
        self.horizontalLayout_3.addWidget(self.btnCancel_tab1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.label_tab2 = QtGui.QLabel(self.tab_2)
        self.label_tab2.setObjectName(_fromUtf8("label_tab2"))
        self.verticalLayout_6.addWidget(self.label_tab2)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.labDEM_tab2 = QtGui.QLabel(self.tab_2)
        self.labDEM_tab2.setObjectName(_fromUtf8("labDEM_tab2"))
        self.verticalLayout_9.addWidget(self.labDEM_tab2)
        self.txtDEM_tab2 = QtGui.QLineEdit(self.tab_2)
        self.txtDEM_tab2.setObjectName(_fromUtf8("txtDEM_tab2"))
        self.verticalLayout_9.addWidget(self.txtDEM_tab2)
        self.labOutput_tab2 = QtGui.QLabel(self.tab_2)
        self.labOutput_tab2.setObjectName(_fromUtf8("labOutput_tab2"))
        self.verticalLayout_9.addWidget(self.labOutput_tab2)
        self.txtOutput_tab2 = QtGui.QLineEdit(self.tab_2)
        self.txtOutput_tab2.setObjectName(_fromUtf8("txtOutput_tab2"))
        self.verticalLayout_9.addWidget(self.txtOutput_tab2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.btnDEM_tab2 = QtGui.QPushButton(self.tab_2)
        self.btnDEM_tab2.setObjectName(_fromUtf8("btnDEM_tab2"))
        self.verticalLayout_8.addWidget(self.btnDEM_tab2)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.btnOutput_tab2 = QtGui.QPushButton(self.tab_2)
        self.btnOutput_tab2.setObjectName(_fromUtf8("btnOutput_tab2"))
        self.verticalLayout_8.addWidget(self.btnOutput_tab2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.btnOk_tab2 = QtGui.QPushButton(self.tab_2)
        self.btnOk_tab2.setObjectName(_fromUtf8("btnOk_tab2"))
        self.horizontalLayout_4.addWidget(self.btnOk_tab2)
        self.btnCancel_tab2 = QtGui.QPushButton(self.tab_2)
        self.btnCancel_tab2.setObjectName(_fromUtf8("btnCancel_tab2"))
        self.horizontalLayout_4.addWidget(self.btnCancel_tab2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem15)
        self.label_tab3 = QtGui.QLabel(self.tab_3)
        self.label_tab3.setObjectName(_fromUtf8("label_tab3"))
        self.verticalLayout_10.addWidget(self.label_tab3)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem16)
        self.line_3 = QtGui.QFrame(self.tab_3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_10.addWidget(self.line_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_11.addWidget(self.label_2)
        self.txtNetwork_tab3 = QtGui.QLineEdit(self.tab_3)
        self.txtNetwork_tab3.setObjectName(_fromUtf8("txtNetwork_tab3"))
        self.verticalLayout_11.addWidget(self.txtNetwork_tab3)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_11.addWidget(self.label_3)
        self.txtDEM_tab3 = QtGui.QLineEdit(self.tab_3)
        self.txtDEM_tab3.setObjectName(_fromUtf8("txtDEM_tab3"))
        self.verticalLayout_11.addWidget(self.txtDEM_tab3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem17)
        self.btnNetwork_tab3 = QtGui.QPushButton(self.tab_3)
        self.btnNetwork_tab3.setObjectName(_fromUtf8("btnNetwork_tab3"))
        self.verticalLayout_12.addWidget(self.btnNetwork_tab3)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem18)
        self.btnDEM_tab3 = QtGui.QPushButton(self.tab_3)
        self.btnDEM_tab3.setObjectName(_fromUtf8("btnDEM_tab3"))
        self.verticalLayout_12.addWidget(self.btnDEM_tab3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem19)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.btnOk_tab3 = QtGui.QPushButton(self.tab_3)
        self.btnOk_tab3.setObjectName(_fromUtf8("btnOk_tab3"))
        self.horizontalLayout_6.addWidget(self.btnOk_tab3)
        self.btnCancel_tab3 = QtGui.QPushButton(self.tab_3)
        self.btnCancel_tab3.setObjectName(_fromUtf8("btnCancel_tab3"))
        self.horizontalLayout_6.addWidget(self.btnCancel_tab3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem21)
        self.label_tab4 = QtGui.QLabel(self.tab_4)
        self.label_tab4.setObjectName(_fromUtf8("label_tab4"))
        self.verticalLayout_13.addWidget(self.label_tab4)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem22)
        self.line_4 = QtGui.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_13.addWidget(self.line_4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_15.addWidget(self.label_4)
        self.txtNetwork_tab4 = QtGui.QLineEdit(self.tab_4)
        self.txtNetwork_tab4.setObjectName(_fromUtf8("txtNetwork_tab4"))
        self.verticalLayout_15.addWidget(self.txtNetwork_tab4)
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_15.addWidget(self.label_5)
        self.txtDEM_tab4 = QtGui.QLineEdit(self.tab_4)
        self.txtDEM_tab4.setObjectName(_fromUtf8("txtDEM_tab4"))
        self.verticalLayout_15.addWidget(self.txtDEM_tab4)
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_15.addWidget(self.label_6)
        self.txtDA_tab4 = QtGui.QLineEdit(self.tab_4)
        self.txtDA_tab4.setObjectName(_fromUtf8("txtDA_tab4"))
        self.verticalLayout_15.addWidget(self.txtDA_tab4)
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_15.addWidget(self.label_7)
        self.txtWidthTable_tab4 = QtGui.QLineEdit(self.tab_4)
        self.txtWidthTable_tab4.setObjectName(_fromUtf8("txtWidthTable_tab4"))
        self.verticalLayout_15.addWidget(self.txtWidthTable_tab4)
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_15.addWidget(self.label_8)
        self.txtEpsg_tab4 = QtGui.QLineEdit(self.tab_4)
        self.txtEpsg_tab4.setObjectName(_fromUtf8("txtEpsg_tab4"))
        self.verticalLayout_15.addWidget(self.txtEpsg_tab4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        spacerItem23 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem23)
        self.btnNetwork_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnNetwork_tab4.setObjectName(_fromUtf8("btnNetwork_tab4"))
        self.verticalLayout_14.addWidget(self.btnNetwork_tab4)
        spacerItem24 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem24)
        self.btnDEM_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnDEM_tab4.setObjectName(_fromUtf8("btnDEM_tab4"))
        self.verticalLayout_14.addWidget(self.btnDEM_tab4)
        spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem25)
        self.btnDA_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnDA_tab4.setObjectName(_fromUtf8("btnDA_tab4"))
        self.verticalLayout_14.addWidget(self.btnDA_tab4)
        spacerItem26 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem26)
        self.btnWidthTable_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnWidthTable_tab4.setObjectName(_fromUtf8("btnWidthTable_tab4"))
        self.verticalLayout_14.addWidget(self.btnWidthTable_tab4)
        spacerItem27 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem27)
        spacerItem28 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem28)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        spacerItem29 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem29)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem30 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem30)
        self.btnOk_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnOk_tab4.setObjectName(_fromUtf8("btnOk_tab4"))
        self.horizontalLayout_8.addWidget(self.btnOk_tab4)
        self.btnCancel_tab4 = QtGui.QPushButton(self.tab_4)
        self.btnCancel_tab4.setObjectName(_fromUtf8("btnCancel_tab4"))
        self.horizontalLayout_8.addWidget(self.btnCancel_tab4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.gridLayout_5.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pre-processing Tools", None))
        self.label_tab1.setText(_translate("MainWindow", "Projects a DEM into a coordinate reference system and then clips it to the extent of a selected watershed", None))
        self.labDEM_tab1.setText(_translate("MainWindow", "DEM", None))
        self.labWats_tab1.setText(_translate("MainWindow", "Watershed", None))
        self.labEpsg_tab1.setText(_translate("MainWindow", "EPSG Number", None))
        self.labOutput_tab1.setText(_translate("MainWindow", "Output DEM", None))
        self.btnDEM_tab1.setText(_translate("MainWindow", ". . .", None))
        self.btnWats_tab1.setText(_translate("MainWindow", ". . .", None))
        self.btnOutput_tab1.setText(_translate("MainWindow", ". . .", None))
        self.btnOk_tab1.setText(_translate("MainWindow", "OK", None))
        self.btnCancel_tab1.setText(_translate("MainWindow", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Watershed DEM", None))
        self.label_tab2.setText(_translate("MainWindow", "Produces a drainage area raster where each cell value is contributing upstream area in square kilomters", None))
        self.labDEM_tab2.setText(_translate("MainWindow", "DEM", None))
        self.labOutput_tab2.setText(_translate("MainWindow", "Drainage Area Raster Ouptut", None))
        self.btnDEM_tab2.setText(_translate("MainWindow", ". . .", None))
        self.btnOutput_tab2.setText(_translate("MainWindow", ". . .", None))
        self.btnOk_tab2.setText(_translate("MainWindow", "OK", None))
        self.btnCancel_tab2.setText(_translate("MainWindow", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Drainage Area", None))
        self.label_tab3.setText(_translate("MainWindow", "Adds fields to an input drainage network representing network topology", None))
        self.label_2.setText(_translate("MainWindow", "Drainage Network", None))
        self.label_3.setText(_translate("MainWindow", "DEM", None))
        self.btnNetwork_tab3.setText(_translate("MainWindow", ". . .", None))
        self.btnDEM_tab3.setText(_translate("MainWindow", ". . .", None))
        self.btnOk_tab3.setText(_translate("MainWindow", "OK", None))
        self.btnCancel_tab3.setText(_translate("MainWindow", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Network Topology", None))
        self.label_tab4.setText(_translate("MainWindow", "Adds slope, drainage area and width attributes to an input drainage network", None))
        self.label_4.setText(_translate("MainWindow", "Drainage Network", None))
        self.label_5.setText(_translate("MainWindow", "DEM", None))
        self.label_6.setText(_translate("MainWindow", "Drainage Area Raster", None))
        self.label_7.setText(_translate("MainWindow", "Width Table (csv)", None))
        self.label_8.setText(_translate("MainWindow", "EPSG Number", None))
        self.btnNetwork_tab4.setText(_translate("MainWindow", ". . .", None))
        self.btnDEM_tab4.setText(_translate("MainWindow", ". . .", None))
        self.btnDA_tab4.setText(_translate("MainWindow", ". . .", None))
        self.btnWidthTable_tab4.setText(_translate("MainWindow", ". . .", None))
        self.btnOk_tab4.setText(_translate("MainWindow", "OK", None))
        self.btnCancel_tab4.setText(_translate("MainWindow", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Network Attributes", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

