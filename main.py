from PySide6.QtWidgets import QApplication
from Views.MenuView import MenuWindow
from Servises.Database import Database

def main():
    Database.initialize()
    app = QApplication([])
    menu_form = MenuWindow()
    menu_form.show()
    app.exec()
    Database.close()

if __name__ == "__main__":
    main()
