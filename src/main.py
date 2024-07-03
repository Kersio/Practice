from PyQt5.QtWidgets import QApplication

from menu_window import MenuWindow

if __name__ == '__main__':
    app = QApplication([])
    ex = MenuWindow()
    app.exec_()