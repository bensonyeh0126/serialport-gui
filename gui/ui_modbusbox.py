from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy

class Ui_ModbusBox(object):
    def setupUi(self, modbusBox):
        modbusBox.setObjectName("modbusBox")

        self.centralWidget = QtWidgets.QWidget(modbusBox)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 300, 240))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.setting_area = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.setting_area.setContentsMargins(10, 10, 10, 10)
        self.setting_area.setSpacing(6)
        self.setting_area.setObjectName("setting_area")
        self.mode_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.setting_area.addWidget(self.mode_comboBox, 0, 1, 1, 1)
        self.mode_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.mode_label.setObjectName("mode_label")
        self.setting_area.addWidget(self.mode_label, 0, 0, 1, 1)
        self.port_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.port_comboBox.setObjectName("port_comboBox")
        self.setting_area.addWidget(self.port_comboBox, 1, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.port_label.setObjectName("port_label")
        self.setting_area.addWidget(self.port_label, 1, 0, 1, 1)
        self.baudrate_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.baudrate_comboBox.setObjectName("baudrate_comboBox")
        self.setting_area.addWidget(self.baudrate_comboBox, 2, 1, 1, 1)
        self.baudrate_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.baudrate_label.setObjectName("baudrate_label")
        self.setting_area.addWidget(self.baudrate_label, 2, 0, 1, 1)
        self.dataBits_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.dataBits_comboBox.setObjectName("dataBits_comboBox")
        self.setting_area.addWidget(self.dataBits_comboBox, 3, 1, 1, 1)
        self.dataBits_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dataBits_label.setObjectName("dataBits_label")
        self.setting_area.addWidget(self.dataBits_label, 3, 0, 1, 1)
        self.stopBits_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.stopBits_comboBox.setObjectName("stopBits_comboBox")
        self.setting_area.addWidget(self.stopBits_comboBox,4, 1, 1, 1)
        self.stopBits_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.stopBits_label.setObjectName("stopBits_label")
        self.setting_area.addWidget(self.stopBits_label, 4, 0, 1, 1)
        self.parity_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.parity_comboBox.setObjectName("parity_comboBox")
        self.setting_area.addWidget(self.parity_comboBox, 5, 1, 1, 1)
        self.parity_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parity_label.setObjectName("parity_label")
        self.setting_area.addWidget(self.parity_label, 5, 0, 1, 1)
        self.slaveID_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.slaveID_comboBox.setObjectName("slaveID_comboBox")
        self.setting_area.addWidget(self.slaveID_comboBox, 6, 1, 1, 1)
        self.slaveID_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.slaveID_label.setObjectName("slaveID_label")
        self.setting_area.addWidget(self.slaveID_label, 6, 0, 1, 1)
        self.openPortBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openPortBtn.setObjectName("openPortBtn")
        self.setting_area.addWidget(self.openPortBtn, 7, 0, 1, 1)
        self.closePortBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.closePortBtn.setObjectName("closePortBtn")
        self.setting_area.addWidget(self.closePortBtn, 7, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(350, 10, 461, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.value_area = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.value_area.setSpacing(6)
        self.value_area.setObjectName("value_area")
        self.sendBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.sendBtn.setObjectName("sendBtn")
        self.value_area.addWidget(self.sendBtn, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 400, 800, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.requestBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.requestBrowser.setObjectName("requestBrowser")
        self.horizontalLayout.addWidget(self.requestBrowser)
        self.responseBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.responseBrowser.setObjectName("responseBrowser")
        self.horizontalLayout.addWidget(self.responseBrowser)
        
        self.retranslateUi(modbusBox)

        self.openPortBtn.clicked.connect(modbusBox.open)
        self.sendBtn.clicked.connect(modbusBox.send)
        '''
        self.openPortBtn.clicked.connect(modbusBox.open)
        self.closePortBtn.clicked.connect(modbusBox.close)
        self.clearBtn.clicked.connect(modbusBox.clear)
        self.recvTextBrowser.cursorPositionChanged.connect(modbusBox.autoScroll)
        self.sendTextButton.clicked.connect(modbusBox.write)
        '''

    def retranslateUi(self, modbusBox):
        _translate = QtCore.QCoreApplication.translate
        modbusBox.setTitle(_translate("ModbusBox", "ModBus Box"))
        self.mode_label.setText(_translate("ModbusBox", "Mode"))
        self.port_label.setText(_translate("ModbusBox", "Port"))
        self.baudrate_label.setText(_translate("ModbusBox", "Baudrate"))
        self.dataBits_label.setText(_translate("ModbusBox", "Data bits"))
        self.stopBits_label.setText(_translate("ModbusBox", "Stop bits"))
        self.parity_label.setText(_translate("ModbusBox", "Parity"))
        self.slaveID_label.setText(_translate("ModbusBox", "Slave ID"))
        self.openPortBtn.setText(_translate("ModbusBox", "Open"))
        self.closePortBtn.setText(_translate("ModbusBox", "Close"))
        self.sendBtn.setText(_translate("ModbusBox", "Send"))
        #self.requestLabel.setText(_translate("ModbusBox", "Request received"))
        #self.responseLabel.setText(_translate("ModbusBox", "Response received"))

    