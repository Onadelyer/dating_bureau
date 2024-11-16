from PySide6.QtWidgets import QMainWindow
from DesignFiles.MenuWindow import Ui_MenuWindow
from Views.AddWindow import AddWindow
from Views.About import About
from Views.Management import Management

class MenuWindow(QMainWindow, Ui_MenuWindow):
    """Головне вікно"""
    def __init__(self, parent=None):
        """Ініціалізація методів та об'єктів на вікні"""
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.AddItems.clicked.connect(self.open_add)
        self.About.clicked.connect(self.open_about)
        self.Management.clicked.connect(self.open_manage)
        self.actionAddData.triggered.connect(self.open_add)
        self.actionManagement.triggered.connect(self.open_manage)
        self.actionAbout.triggered.connect(self.open_about)

    def open_manage(self):
        """Відкриття форми для керування даними"""
        self.manage = Management()
        self.manage.show()

    def open_add(self):
        """Відкриття форми для додавання даних"""
        self.add_window = AddWindow()
        self.add_window.show()

    def open_about(self):
        """Відкриття вікна про програму"""
        self.about = About()
        self.about.show()
