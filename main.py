from PyQt6 import QtCore, QtWidgets, uic
import thread


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = uic.loadUi("enercom.ui")
        # Здесь можно изменять параметры окна
        self.ui.show()
        self.labels = [self.ui.p1_0_0, self.ui.p1_0_1, self.ui.p1_0_2, self.ui.p1_0_3,
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

                       self.ui.p3_0_0, self.ui.p3_0_1, self.ui.p3_0_2, self.ui.p3_0_3,
                       self.ui.p3_0_4, self.ui.p3_0_5, self.ui.p3_0_6, self.ui.p3_0_7,
                       self.ui.p3_1_0, self.ui.p3_1_1, self.ui.p3_1_2, self.ui.p3_1_3,
                       self.ui.p3_1_4, self.ui.p3_1_5, self.ui.p3_1_6, self.ui.p3_1_7,
                       self.ui.p3_2_0, self.ui.p3_2_1, self.ui.p3_2_2, self.ui.p3_2_3,
                       self.ui.p3_2_4, self.ui.p3_2_5, self.ui.p3_2_6, self.ui.p3_2_7,
                       self.ui.p3_3_0, self.ui.p3_3_1, self.ui.p3_3_2, self.ui.p3_3_3,
                       self.ui.p3_3_4, self.ui.p3_3_5, self.ui.p3_3_6, self.ui.p3_3_7,

                       self.ui.p4_0_0, self.ui.p4_0_1, self.ui.p4_0_2, self.ui.p4_0_3,
                       self.ui.p4_0_4, self.ui.p4_0_5, self.ui.p4_0_6, self.ui.p4_0_7,
                       self.ui.p4_1_0, self.ui.p4_1_1, self.ui.p4_1_2, self.ui.p4_1_3,
                       self.ui.p4_1_4, self.ui.p4_1_5, self.ui.p4_1_6, self.ui.p4_1_7,
                       self.ui.p4_2_0, self.ui.p4_2_1, self.ui.p4_2_2, self.ui.p4_2_3,
                       self.ui.p4_2_4, self.ui.p4_2_5, self.ui.p4_2_6, self.ui.p4_2_7,
                       self.ui.p4_3_0, self.ui.p4_3_1, self.ui.p4_3_2, self.ui.p4_3_3,
                       self.ui.p4_3_4, self.ui.p4_3_5, self.ui.p4_3_6, self.ui.p4_3_7,

                       self.ui.p5_0_0, self.ui.p5_0_1, self.ui.p5_0_2, self.ui.p5_0_3,
                       self.ui.p5_0_4, self.ui.p5_0_5, self.ui.p5_0_6, self.ui.p5_0_7,
                       self.ui.p5_1_0, self.ui.p5_1_1, self.ui.p5_1_2, self.ui.p5_1_3,
                       self.ui.p5_1_4, self.ui.p5_1_5, self.ui.p5_1_6, self.ui.p5_1_7,
                       self.ui.p5_2_0, self.ui.p5_2_1, self.ui.p5_2_2, self.ui.p5_2_3,
                       self.ui.p5_2_4, self.ui.p5_2_5, self.ui.p5_2_6, self.ui.p5_2_7,
                       self.ui.p5_3_0, self.ui.p5_3_1, self.ui.p5_3_2, self.ui.p5_3_3,
                       self.ui.p5_3_4, self.ui.p5_3_5, self.ui.p5_3_6, self.ui.p5_3_7,

                       self.ui.p6_0_0, self.ui.p6_0_1, self.ui.p6_0_2, self.ui.p6_0_3,
                       self.ui.p6_0_4, self.ui.p6_0_5, self.ui.p6_0_6, self.ui.p6_0_7,
                       self.ui.p6_1_0, self.ui.p6_1_1, self.ui.p6_1_2, self.ui.p6_1_3,
                       self.ui.p6_1_4, self.ui.p6_1_5, self.ui.p6_1_6, self.ui.p6_1_7,
                       self.ui.p6_2_0, self.ui.p6_2_1, self.ui.p6_2_2, self.ui.p6_2_3,
                       self.ui.p6_2_4, self.ui.p6_2_5, self.ui.p6_2_6, self.ui.p6_2_7,
                       self.ui.p6_3_0, self.ui.p6_3_1, self.ui.p6_3_2, self.ui.p6_3_3,
                       self.ui.p6_3_4, self.ui.p6_3_5, self.ui.p6_3_6, self.ui.p6_3_7,

                       self.ui.p7_0_0, self.ui.p7_0_1, self.ui.p7_0_2, self.ui.p7_0_3,
                       self.ui.p7_0_4, self.ui.p7_0_5, self.ui.p7_0_6, self.ui.p7_0_7,
                       self.ui.p7_1_0, self.ui.p7_1_1, self.ui.p7_1_2, self.ui.p7_1_3,
                       self.ui.p7_1_4, self.ui.p7_1_5, self.ui.p7_1_6, self.ui.p7_1_7,
                       self.ui.p7_2_0, self.ui.p7_2_1, self.ui.p7_2_2, self.ui.p7_2_3,
                       self.ui.p7_2_4, self.ui.p7_2_5, self.ui.p7_2_6, self.ui.p7_2_7,
                       self.ui.p7_3_0, self.ui.p7_3_1, self.ui.p7_3_2, self.ui.p7_3_3,
                       self.ui.p7_3_4, self.ui.p7_3_5, self.ui.p7_3_6, self.ui.p7_3_7,

                       self.ui.p8_0_0, self.ui.p8_0_1, self.ui.p8_0_2, self.ui.p8_0_3,
                       self.ui.p8_0_4, self.ui.p8_0_5, self.ui.p8_0_6, self.ui.p8_0_7,
                       self.ui.p8_1_0, self.ui.p8_1_1, self.ui.p8_1_2, self.ui.p8_1_3,
                       self.ui.p8_1_4, self.ui.p8_1_5, self.ui.p8_1_6, self.ui.p8_1_7,
                       self.ui.p8_2_0, self.ui.p8_2_1, self.ui.p8_2_2, self.ui.p8_2_3,
                       self.ui.p8_2_4, self.ui.p8_2_5, self.ui.p8_2_6, self.ui.p8_2_7,
                       self.ui.p8_3_0, self.ui.p8_3_1, self.ui.p8_3_2, self.ui.p8_3_3,
                       self.ui.p8_3_4, self.ui.p8_3_5, self.ui.p8_3_6, self.ui.p8_3_7,

                       self.ui.p9_0_0, self.ui.p9_0_1, self.ui.p9_0_2, self.ui.p9_0_3,
                       self.ui.p9_0_4, self.ui.p9_0_5, self.ui.p9_0_6, self.ui.p9_0_7,
                       self.ui.p9_1_0, self.ui.p9_1_1, self.ui.p9_1_2, self.ui.p9_1_3,
                       self.ui.p9_1_4, self.ui.p9_1_5, self.ui.p9_1_6, self.ui.p9_1_7,
                       self.ui.p9_2_0, self.ui.p9_2_1, self.ui.p9_2_2, self.ui.p9_2_3,
                       self.ui.p9_2_4, self.ui.p9_2_5, self.ui.p9_2_6, self.ui.p9_2_7,
                       self.ui.p9_3_0, self.ui.p9_3_1, self.ui.p9_3_2, self.ui.p9_3_3,
                       self.ui.p9_3_4, self.ui.p9_3_5, self.ui.p9_3_6, self.ui.p9_3_7,

                       self.ui.p10_0_0, self.ui.p10_0_1, self.ui.p10_0_2, self.ui.p10_0_3,
                       self.ui.p10_0_4, self.ui.p10_0_5, self.ui.p10_0_6, self.ui.p10_0_7,
                       self.ui.p10_1_0, self.ui.p10_1_1, self.ui.p10_1_2, self.ui.p10_1_3,
                       self.ui.p10_1_4, self.ui.p10_1_5, self.ui.p10_1_6, self.ui.p10_1_7,
                       self.ui.p10_2_0, self.ui.p10_2_1, self.ui.p10_2_2, self.ui.p10_2_3,
                       self.ui.p10_2_4, self.ui.p10_2_5, self.ui.p10_2_6, self.ui.p10_2_7,
                       self.ui.p10_3_0, self.ui.p10_3_1, self.ui.p10_3_2, self.ui.p10_3_3,
                       self.ui.p10_3_4, self.ui.p10_3_5, self.ui.p10_3_6, self.ui.p10_3_7,

                       self.ui.p11_0_0, self.ui.p11_0_1, self.ui.p11_0_2, self.ui.p11_0_3,
                       self.ui.p11_0_4, self.ui.p11_0_5, self.ui.p11_0_6, self.ui.p11_0_7,
                       self.ui.p11_1_0, self.ui.p11_1_1, self.ui.p11_1_2, self.ui.p11_1_3,
                       self.ui.p11_1_4, self.ui.p11_1_5, self.ui.p11_1_6, self.ui.p11_1_7,
                       self.ui.p11_2_0, self.ui.p11_2_1, self.ui.p11_2_2, self.ui.p11_2_3,
                       self.ui.p11_2_4, self.ui.p11_2_5, self.ui.p11_2_6, self.ui.p11_2_7,
                       self.ui.p11_3_0, self.ui.p11_3_1, self.ui.p11_3_2, self.ui.p11_3_3,
                       self.ui.p11_3_4, self.ui.p11_3_5, self.ui.p11_3_6, self.ui.p11_3_7,

                       self.ui.p12_0_0, self.ui.p12_0_1, self.ui.p12_0_2, self.ui.p12_0_3,
                       self.ui.p12_0_4, self.ui.p12_0_5, self.ui.p12_0_6, self.ui.p12_0_7,
                       self.ui.p12_1_0, self.ui.p12_1_1, self.ui.p12_1_2, self.ui.p12_1_3,
                       self.ui.p12_1_4, self.ui.p12_1_5, self.ui.p12_1_6, self.ui.p12_1_7,
                       self.ui.p12_2_0, self.ui.p12_2_1, self.ui.p12_2_2, self.ui.p12_2_3,
                       self.ui.p12_2_4, self.ui.p12_2_5, self.ui.p12_2_6, self.ui.p12_2_7,
                       self.ui.p12_3_0, self.ui.p12_3_1, self.ui.p12_3_2, self.ui.p12_3_3,
                       self.ui.p12_3_4, self.ui.p12_3_5, self.ui.p12_3_6, self.ui.p12_3_7, ]

        self.ui.btn_connect.clicked.connect(self.connect_serial)
        self.connection_flag = 0

        self.ui.btn_scan.clicked.connect(self.cmb_data)

        self.com_thread = thread.ComThread()
        self.com_thread.serial_data.connect(self.on_change, QtCore.Qt.ConnectionType.QueuedConnection)
        self.cmb_data()

    def connect_serial(self):
        if self.connection_flag == 0:
            self.connection_flag = 1
            self.com_thread.open_port(self.ui.cmb_serial_ports.currentText())
            self.ui.btn_connect.setText("Отключиться")
            self.ui.btn_scan.setDisabled(True)
        else:
            self.connection_flag = 0
            self.com_thread.close_port()
            self.ui.btn_connect.setText("Подключиться")
            self.ui.btn_scan.setDisabled(False)

    def cmb_data(self):
        self.ui.cmb_serial_ports.clear()
        self.ui.cmb_serial_ports.addItems(self.com_thread.find_serial_ports())

    def on_change(self, s):
        #print(s)

        a = 0
        while a < 48:
            i = 0
            while i < 8:
                if s[a + 5] & (1 << i):
                    self.labels[i + (8 * a)].setStyleSheet("background-color : green")
                if not s[a + 5] & (1 << i):
                    self.labels[i + (8 * a)].setStyleSheet("background-color : #f95a5a")
                i = i + 1
            a = a + 1

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
