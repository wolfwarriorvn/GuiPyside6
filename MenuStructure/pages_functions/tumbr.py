from PySide6.QtWidgets import QWidget

from ui.pages.ui_tumbr import Ui_Form

class Tumbr(QWidget):
    def __init__(self):
        super(Tumbr, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        