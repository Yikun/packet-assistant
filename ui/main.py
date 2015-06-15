# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainUI(object):
    def setupUi(self, MainUI):
        MainUI.setObjectName(_fromUtf8("MainUI"))
        MainUI.resize(581, 341)
        self.centralwidget = QtGui.QWidget(MainUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 301))
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 541, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 24))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 40, 24))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(450, 20, 31, 24))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.daEdit = QtGui.QLineEdit(self.groupBox)
        self.daEdit.setGeometry(QtCore.QRect(50, 20, 143, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.daEdit.setFont(font)
        self.daEdit.setObjectName(_fromUtf8("daEdit"))
        self.saEdit = QtGui.QLineEdit(self.groupBox)
        self.saEdit.setGeometry(QtCore.QRect(270, 20, 143, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saEdit.setFont(font)
        self.saEdit.setObjectName(_fromUtf8("saEdit"))
        self.typeEdit = QtGui.QLineEdit(self.groupBox)
        self.typeEdit.setGeometry(QtCore.QRect(480, 20, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.typeEdit.setFont(font)
        self.typeEdit.setObjectName(_fromUtf8("typeEdit"))
        self.netSelBtn = QtGui.QPushButton(self.tab)
        self.netSelBtn.setGeometry(QtCore.QRect(480, 10, 61, 26))
        self.netSelBtn.setObjectName(_fromUtf8("netSelBtn"))
        self.netSelCombo = QtGui.QComboBox(self.tab)
        self.netSelCombo.setEnabled(True)
        self.netSelCombo.setGeometry(QtCore.QRect(10, 10, 461, 22))
        self.netSelCombo.setObjectName(_fromUtf8("netSelCombo"))
        self.frameCombo = QtGui.QComboBox(self.tab)
        self.frameCombo.setEnabled(False)
        self.frameCombo.setGeometry(QtCore.QRect(50, 250, 151, 22))
        self.frameCombo.setObjectName(_fromUtf8("frameCombo"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.autoTimeEdit = QtGui.QLineEdit(self.tab)
        self.autoTimeEdit.setEnabled(False)
        self.autoTimeEdit.setGeometry(QtCore.QRect(230, 250, 51, 20))
        self.autoTimeEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.autoTimeEdit.setObjectName(_fromUtf8("autoTimeEdit"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(290, 250, 21, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.sendBtn = QtGui.QPushButton(self.tab)
        self.sendBtn.setEnabled(False)
        self.sendBtn.setGeometry(QtCore.QRect(484, 248, 61, 26))
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.autoSendBtn = QtGui.QPushButton(self.tab)
        self.autoSendBtn.setEnabled(False)
        self.autoSendBtn.setGeometry(QtCore.QRect(310, 248, 61, 26))
        self.autoSendBtn.setObjectName(_fromUtf8("autoSendBtn"))
        self.payloadEdit = QtGui.QPlainTextEdit(self.tab)
        self.payloadEdit.setGeometry(QtCore.QRect(10, 100, 541, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.payloadEdit.setFont(font)
        self.payloadEdit.setObjectName(_fromUtf8("payloadEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        MainUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainUI.setStatusBar(self.statusbar)

        self.retranslateUi(MainUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

    def retranslateUi(self, MainUI):
        MainUI.setWindowTitle(_translate("MainUI", "PacketAssist", None))
        self.groupBox.setTitle(_translate("MainUI", "Layer 2 Header", None))
        self.label.setText(_translate("MainUI", "MAC DA:", None))
        self.label_2.setText(_translate("MainUI", "MAC SA:", None))
        self.label_3.setText(_translate("MainUI", "Type:", None))
        self.daEdit.setText(_translate("MainUI", "FF FF FF FF FF FF", None))
        self.saEdit.setText(_translate("MainUI", "FF FF FF FF FF FF", None))
        self.typeEdit.setText(_translate("MainUI", "08 FF", None))
        self.netSelBtn.setText(_translate("MainUI", "确认选择", None))
        self.label_7.setText(_translate("MainUI", "帧模板", None))
        self.autoTimeEdit.setText(_translate("MainUI", "1000", None))
        self.label_8.setText(_translate("MainUI", "ms", None))
        self.sendBtn.setText(_translate("MainUI", "发送一次", None))
        self.autoSendBtn.setText(_translate("MainUI", "自动发送", None))
        self.payloadEdit.setPlainText(_translate("MainUI", "45 05 00 32 00 00 00 00 01 02 D8 19 C0 A8 40 01 E0 01 01 01 16 03 08 FA E0 01 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainUI", "以太网", None))

