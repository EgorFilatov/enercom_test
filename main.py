from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import thread


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
