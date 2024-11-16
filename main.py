from PySide6.QtWidgets import QApplication
from Views.MenuView import MenuWindow

def main():
    app = QApplication([])
    menu_form = MenuWindow()
    menu_form.show()
    app.exec()

if __name__ == "__main__":
    main()
