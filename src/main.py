from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Основной горизонтальный layout
        hbox = QHBoxLayout(self)

        # Вертикальный layout для кнопок
        vbox_buttons = QVBoxLayout()

        # Создание и добавление кнопок в вертикальный layout
        for i in range(1, 7):
            button = QPushButton(f'Кнопка {i}', self)
            vbox_buttons.addWidget(button)

        # Добавление вертикального layout с кнопками в горизонтальный layout
        hbox.addLayout(vbox_buttons)

        # Метка для изображения с правой стороны
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap('path_to_image.jpg'))  # Укажите путь к вашему изображению
        hbox.addWidget(self.image_label)

        # Установка основного layout для виджета
        self.setLayout(hbox)

        # Установка размера и заголовка основного окна
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Окно с кнопками и изображением')
        self.show()


# Запуск приложения
if __name__ == '__main__':
    app = QApplication([])
    ex = ExampleApp()
    app.exec_()