# pylint: disable=comparison-with-itself
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui.ui_main_window import Ui_MainWindow

from pages_functions.home import Home
from pages_functions.dashboard import Dashboard
from pages_functions.lexus import Lexus
from pages_functions.mazda import Mazda
from pages_functions.toyota import Toyota
from pages_functions.tumbr import Tumbr
from pages_functions.youtube import Youtube

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        "Create a dick for menu button and tab windows"
        self.menu_btn_dict = {
            self.btn_home: Home(),
            self.btn_dashboard: Dashboard(),
            self.btn_toyota: Toyota(),
            self.btn_lexus: Lexus(),
            self.btn_mazda: Mazda(),
            self.btn_youtube: Youtube(),
            self.btn_tumb: Tumbr()
        }
        "Show home window"
        self.show_home_window()

        "Connect signal and slot"
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.btn_home.clicked.connect(self.show_selected_window)
        self.btn_dashboard.clicked.connect(self.show_selected_window)
        self.btn_lexus.clicked.connect(self.show_selected_window)
        self.btn_mazda.clicked.connect(self.show_selected_window)
        self.btn_toyota.clicked.connect(self.show_selected_window)
        self.btn_tumb.clicked.connect(self.show_selected_window)
        self.btn_youtube.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.btn_home)
        self.set_btn_checked(self.btn_home)

        if result[0]:
            self.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.btn_home.text()
            curIndex = self.tabWidget.addTab(Home(), tab_title)
            self.tabWidget.setCurrentIndex(curIndex)
            self.tabWidget.setVisible(True)

    
    def set_btn_checked(self, btn):
        for button in self.menu_btn_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)


    def close_tab(self, index):
        self.tabWidget.removeTab(index)

        if self.tabWidget.count() == 0:
            self.toolBox.setCurrentIndex(0)
            self.show_home_window()
    def show_selected_window(self):
        button = self.sender()
        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.tabWidget.addTab(self.menu_btn_dict[button], tab_title)
            self.tabWidget.setCurrentIndex(curIndex)
            self.tabWidget.setVisible(True)

    def open_tab_flag(self, btn_text):
        open_tab_count = self.tabWidget.count()

        for i in range(open_tab_count):
            tab_title = self.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i
            else:
                continue
        return False,




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())