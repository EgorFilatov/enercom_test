from PyQt6 import QtCore, QtSerialPort, uic
import re
import main


class ComThread(QtCore.QThread):
    serial_data = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.serial_port = QtSerialPort.QSerialPort()
        self.serial_port.setBaudRate(115200)
        self.serial_port.readyRead.connect(self.read_data)
        self.received_data_previous = ""
        self.received_data_full_int = []

    def find_available_serial_ports(self):
        self.available_serial_ports = []
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            self.available_serial_ports.append(port.portName())
        return self.available_serial_ports

    def open_port(self, port_name):
        self.serial_port.setPortName(port_name)
        self.serial_port.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)

    def close_port(self):
        self.serial_port.close()

    def read_data(self):
        self.received_data = str(self.serial_port.readAll().toHex()).replace('b', '').replace("'", '')
        print(self.received_data)
        self.ready_to_convert_flag = 0
        self.received_data_full = ""
        if len(self.received_data) > 0 and self.received_data[0] == '5' and self.received_data[1] == '5':
            self.ready_to_convert_flag = 1
            self.received_data_full = self.received_data_previous
            self.received_data_previous = self.received_data
        else:
            self.received_data_previous = self.received_data_previous + self.received_data

        if self.ready_to_convert_flag == 1:
            self.convert_data_to_int(self.received_data_full)

    def convert_data_to_int(self, data):
        data = re.findall('.{%s}' % 2, data)
        data_int = []
        for el in data:
            data_int.append(int(el, 16))
        self.received_data_full_int = data_int
        self.turn_on()


    def turn_on(self):
        if len(self.received_data_full_int) > 0:
            self.serial_data.emit(self.received_data_full_int)

    def run(self):
        True

