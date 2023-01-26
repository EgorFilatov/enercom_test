import sys
import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtCore
from PyQt6.QtCore import QThread, QIODevice
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6 import uic


class SerialData(QThread):
    serial_port = QSerialPort()

    def __init__(self):
        QThread.__init__(self)
        #self.serial_port.readyRead.connect(print("a"))


    def open_port(self, port_name):
        self.serial_port.setBaudRate(115200)
        self.serial_port.setPortName(port_name)
        #self.serial_port.open(QIODevice.OpenModeFlag.ReadWrite)
        r = self.serial_port.open(QIODevice.OpenModeFlag.ReadWrite)
        if not r:
            print('Port open error')
        else:
            print('Port opened')
            self.serial_port.readyRead.connect(self.com_read_data())
        #self.serial_port.readyRead.connect(self.read_from_port())

    def close_port(self):
        self.serial_port.close()

    def find_available_serial_ports(self):
        available_serial_ports = []
        for port in QSerialPortInfo.availablePorts():
            available_serial_ports.append(port.portName())
        return available_serial_ports

    def read_from_port(self):
        print("a")
        #rx = self.serial_port.readAll()
        #print(rx)




class App(QWidget):
    serial = SerialData()
    print()

    def __init__(self):
        QWidget.__init__(self)
        self.ui = uic.loadUi("enercom.ui")
        self.ui.show()
        self.button_actions()
        self.cmb_data()

    def button_actions(self):
        self.ui.btn_connect.clicked.connect(lambda: self.click(button_name="btn_connect"))
        self.ui.btn_disconnect.clicked.connect(lambda: self.click(button_name="btn_disconnect"))

    def cmb_data(self):
        self.ui.cmb_availiable_serial_ports.addItems(self.serial.find_available_serial_ports())

    def click(self, button_name=""):
        labels = [self.ui.p1_0_0, self.ui.p1_0_1, self.ui.p1_0_2, self.ui.p1_0_3,
                  self.ui.p1_0_4, self.ui.p1_0_5, self.ui.p1_0_6, self.ui.p1_0_7,
                  self.ui.p1_1_0, self.ui.p1_1_1, self.ui.p1_1_2, self.ui.p1_1_3,
                  self.ui.p1_1_4, self.ui.p1_1_5, self.ui.p1_1_6, self.ui.p1_1_7,
                  self.ui.p1_2_0, self.ui.p1_2_1, self.ui.p1_2_2, self.ui.p1_2_3,
                  self.ui.p1_2_4, self.ui.p1_2_5, self.ui.p1_2_6, self.ui.p1_2_7,
                  self.ui.p1_3_0, self.ui.p1_3_1, self.ui.p1_3_2, self.ui.p1_3_3,
                  self.ui.p1_3_4, self.ui.p1_3_5, self.ui.p1_3_6, self.ui.p1_3_7,

                  self.ui.p2_0_0, self.ui.p2_0_1, self.ui.p2_0_2, self.ui.p2_0_3,
                  self.ui.p2_0_4, self.ui.p2_0_5, self.ui.p2_0_6, self.ui.p2_0_7,
                  self.ui.p2_1_0, self.ui.p2_1_1, self.ui.p2_1_2, self.ui.p2_1_3,
                  self.ui.p2_1_4, self.ui.p2_1_5, self.ui.p2_1_6, self.ui.p2_1_7,
                  self.ui.p2_2_0, self.ui.p2_2_1, self.ui.p2_2_2, self.ui.p2_2_3,
                  self.ui.p2_2_4, self.ui.p2_2_5, self.ui.p2_2_6, self.ui.p2_2_7,
                  self.ui.p2_3_0, self.ui.p2_3_1, self.ui.p2_3_2, self.ui.p2_3_3,
                  self.ui.p2_3_4, self.ui.p2_3_5, self.ui.p2_3_6, self.ui.p2_3_7,
                  ]
        if button_name == "btn_connect":
            self.serial.open_port(self.ui.cmb_availiable_serial_ports.currentText())

        if button_name == "btn_disconnect":
            self.serial.close_port()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
