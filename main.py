from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import thread


<<<<<<< HEAD
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
=======
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
>>>>>>> 3019151596a31ffa7c31669a3297d15ec40ce764
        self.ui = uic.loadUi("enercom.ui")
        self.ui.show()
        self.ui.btn_connect.clicked.connect(self.show_connect)
        self.ui.btn_disconnect.setDisabled(True)
        self.ui.btn_disconnect.clicked.connect(self.show_disconnect)
        self.com_thread = thread.ComThread()
        self.cmb_data()

        self.com_thread.serial_data.connect(self.on_change, QtCore.Qt.ConnectionType.QueuedConnection)

    def cmb_data(self):
        self.ui.cmb_availiable_serial_ports.addItems(self.com_thread.find_available_serial_ports())

    def show_connect(self):
        self.com_thread.open_port(self.ui.cmb_availiable_serial_ports.currentText())
        self.turn_on_label()

        self.ui.lbl_connection_status.setText("Подключено")
        self.ui.btn_connect.setDisabled(True)
        self.ui.btn_disconnect.setDisabled(False)
        self.ui.p1_0_0.setStyleSheet("background-color : green")

    def show_disconnect(self):
        self.com_thread.close_port()

        self.ui.lbl_connection_status.setText("")
        self.ui.btn_disconnect.setDisabled(True)
        self.ui.btn_connect.setDisabled(False)
        self.ui.p1_0_0.setStyleSheet("background-color : red")

    def turn_on_label(self):
        a = 0
        #print(self.com_thread.received_data_full_int)
        #if self.com_thread.received_data_full_int[0] & (1 << 0):
        #    self.ui.p1_0_1.setStyleSheet("background-color : green")

    def on_change(self, s):
        print(s)


if __name__ == '__main__':
<<<<<<< HEAD
    app = QApplication(sys.argv)
    ex = App()
=======
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
>>>>>>> 3019151596a31ffa7c31669a3297d15ec40ce764
    sys.exit(app.exec())
