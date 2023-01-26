from PyQt6 import QtCore
from PyQt6.QtCore import QThread
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtCore import QIODevice

class SerialData(QThread):
    def __init__(self):
        self.serial_port = QSerialPort()

    def open_port(self, flag):
        if flag:
            self.serial_port.setBaudRate(self.toolBar.baudRate())
            self.serial_port.setPortName(self.toolBar.portName())

            r = self.port.open(QtCore.QIODevice.ReadWrite)

        else:
            self.port.close()


