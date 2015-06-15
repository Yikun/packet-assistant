# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from ui.main import Ui_MainUI
from ethernet import Ethernet


class MainWindows(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.ui = Ui_MainUI()
        self.ethnet = Ethernet()
        self.timer = QtCore.QTimer()
        # Init ui
        self.ui.setupUi(self)
        self.ui.netSelCombo.addItems(self.ethnet.devices())
        # Init auto-send timer
        self.connect(
            self.timer, QtCore.SIGNAL("timeout()"), self.on_sendBtn_clicked)

        frameitems = ['IGMP Report', 'IGMP Leave',
                      'IGMP General Query', 'IGMP Specific Query']
        self.ui.frameCombo.addItems(frameitems)

    @QtCore.pyqtSlot()
    def on_sendBtn_clicked(self):
        # Get all data
        sendData = str(self.ui.daEdit.text())
        sendData += str(self.ui.saEdit.text())
        sendData += str(self.ui.typeEdit.text())
        sendData += str(self.ui.payloadEdit.toPlainText())
        # Send packet
        self.ethnet.sendHex(sendData)
        # Packet count ++
        self.ui.statusbar.showMessage("Send Times: " + str(self.ethnet.sendtimes()))

    @QtCore.pyqtSlot()
    def on_autoSendBtn_clicked(self):
        btnText = self.ui.autoSendBtn.text()
        if btnText == u"自动发送":
            self.ui.autoSendBtn.setText(u"停止发送")
            self.ui.autoTimeEdit.setEnabled(False)
            # Start auto send time
            self.timer.start(int(self.ui.autoTimeEdit.text()))
        else:
            self.ui.autoSendBtn.setText(u"自动发送")
            self.ui.autoTimeEdit.setEnabled(True)
            # Stop auto send time
            self.timer.stop()

    @QtCore.pyqtSlot()
    def on_netSelBtn_clicked(self):
        btnText = self.ui.netSelBtn.text()
        if btnText == u"确认选择":
            self.ui.netSelBtn.setText(u"取消选择")
            self.ui.sendBtn.setEnabled(True)
            self.ui.frameCombo.setEnabled(True)
            self.ui.autoSendBtn.setEnabled(True)
            self.ui.autoTimeEdit.setEnabled(True)
            self.ui.netSelCombo.setEnabled(False)
            # Open the current select device
            devName = self.ui.netSelCombo.currentText()
            self.ethnet.open(devName)
            self.ui.statusbar.showMessage(
                "Open: " + devName + ":" + self.ethnet.address())
        else:
            self.ui.netSelBtn.setText(u"确认选择")
            self.ui.sendBtn.setEnabled(False)
            self.ui.frameCombo.setEnabled(False)
            self.ui.autoSendBtn.setEnabled(False)
            self.ui.autoTimeEdit.setEnabled(False)
            self.ui.netSelCombo.setEnabled(True)

    @QtCore.pyqtSlot('const QString&')
    def on_netSelCombo_currentIndexChanged(self, item):
        self.ui.statusbar.showMessage("Select Net: " + item)

    @QtCore.pyqtSlot('const QString&')
    def on_frameCombo_currentIndexChanged(self, item):

        if item == 'IGMP Report':
            da = '01 00 5E 01 01 01'
            sa = '01 00 5E 01 01 01'
            payload = '45 05 00 32 00 00 00 00 01 02 D8 19 C0 A8 40 01 E0 01 01 01 16 03 08 FA E0 01 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        elif item == "IGMP Leave":
            da = '01 00 5E 01 01 01'
            sa = '01 00 5E 01 01 01'
            payload = '45 05 00 32 00 00 00 00 01 02 D8 19 C0 A8 40 01 E0 01 01 01 17 00 07 FD E0 01 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        elif item == "IGMP General Query":
            da = '01 00 5E 01 01 01'
            sa = '01 00 5E 01 01 01'
            payload = '45 05 00 32 00 00 00 00 01 02 D9 1B C0 A8 40 01 E0 00 00 00 11 03 F9 0D E0 01 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        elif item == "IGMP Specific Query":
            da = '01 00 5E 01 01 01'
            sa = '01 00 5E 01 01 01'
            payload = '45 05 00 32 00 00 00 00 01 02 D8 19 C0 A8 40 01 E0 01 01 01 11 03 F9 0D E0 01 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        self.ui.daEdit.setText(da)
        self.ui.saEdit.setText(sa)
        self.ui.payloadEdit.setPlainText(payload)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainwindows = MainWindows()
    mainwindows.show()
    sys.exit(app.exec_())
