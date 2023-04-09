from PySide6.QtWidgets import QWidget

from ui.pages.ui_home import Ui_Form

class Toyota(QWidget):
    def __int__(self):
        super(Toyota).__int__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        