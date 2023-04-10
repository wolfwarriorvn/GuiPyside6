from PySide6.QtWidgets import QWidget

from ui.pages.ui_home import Ui_Form

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)




        