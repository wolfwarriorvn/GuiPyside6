from PySide6.QtWidgets import QWidget

from ui.pages.ui_dashboard import Ui_Form

class Dashboard(QWidget):
    def __int__(self):
        super(Dashboards).__int__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        