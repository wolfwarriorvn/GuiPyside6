import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui.ui_main_window import Ui_MainWindow
from db_connection import Data
from PySide6.QtSql import QSqlTableModel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.btn_add.clicked.connect(self.add_new_user)

    def add_new_user(self):
        user_input = self.le_user_pass.text().split('|')
        self.conn.add_usernick_query(uid=user_input[0], pw=user_input[1])
        self.view_data()
    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('accounts')
        self.model.select()
        self.tableView.setModel(self.model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())