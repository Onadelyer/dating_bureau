from PySide6.QtWidgets import QWidget
from DesignFiles.AboutDesign import Ui_About

class About(QWidget, Ui_About):
    """Вікно з інформацією про програму"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
