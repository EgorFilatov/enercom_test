from PyQt6 import QtCore, QtSerialPort
import re


class ComThread(QtCore.QThread):
    serial_data = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.enercom_message_str = ""

        self.serial_port = QtSerialPort.QSerialPort()
        self.serial_port.setBaudRate(115200)

        #self.serial_port.readyRead.connect(self.start)

    def find_serial_ports(self):
        serial_ports = []
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            serial_ports.append(port.portName())
        return serial_ports

    def open_port(self, port_name):
        self.serial_port.setPortName(port_name)
        self.serial_port.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)

    def close_port(self):
        self.serial_port.close()

    def read_data(self):
        True
        #self.received_data = str(self.serial_port.readAll().toHex()).replace('b', '').replace("'", '')
        #print(self.received_data)


        #received_data = str(self.serial_port.readAll().toHex()).replace('b', '').replace("'", '')
        #if received_data[0] == '5' and received_data[1] == '5':
        #    self.enercom_message_str = received_data
        #else:
        #    self.enercom_message_str = self.enercom_message_str + received_data
        #if len(self.enercom_message_str) == 110:
        #    self.enercom_message_str = re.findall('.{%s}' % 2, self.enercom_message_str)
        #    enercom_message_int = []
        #    for el in self.enercom_message_str:
        #        enercom_message_int.append(int(el, 16))
        #    if len(enercom_message_int) > 0:
        #        print(enercom_message_int)
        #        self.serial_data.emit(enercom_message_int)



    def run(self):
        while True:
            if self.serial_port.waitForReadyRead():
                #received_data = str(self.serial_port.readAll().toHex()).replace('b', '').replace("'", '')
                received_data = self.serial_port.readAll()
                r = received_data.toInt()
                print(r)
                if received_data[0] == '5' and received_data[1] == '5':
                    self.enercom_message_str = received_data
                else:
                    self.enercom_message_str = self.enercom_message_str + received_data
                if len(self.enercom_message_str) == 110:
                    self.enercom_message_str = re.findall('.{%s}' % 2, self.enercom_message_str)
                    enercom_message_int = []
                    for el in self.enercom_message_str:
                        enercom_message_int.append(int(el, 16))
                    if len(enercom_message_int) > 0:
                        True
                        #print(enercom_message_int)
                        #self.serial_data.emit(enercom_message_int)








