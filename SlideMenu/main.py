import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_test.clicked.connect(self.open_test)

    def open_test(self):
        lb_text = self.lb_info.text()
        print("test now")
        print(lb_text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())