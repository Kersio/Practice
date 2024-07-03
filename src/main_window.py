from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self, frame):
        super().__init__()
        self.initUI(frame)

    def initUI(self, frame):
        # Основной виджет и макеты
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Макет для кнопок слева
        self.buttons_layout = QVBoxLayout()

        # Создание и добавление кнопок
        self.button1 = QPushButton('Кнопка 1', self)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.buttons_layout.addWidget(self.button1)

        self.button2 = QPushButton('Кнопка 2', self)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.buttons_layout.addWidget(self.button2)

        self.button3 = QPushButton('Кнопка 3', self)
        self.button3.clicked.connect(self.on_button3_clicked)
        self.buttons_layout.addWidget(self.button3)

        self.button4 = QPushButton('Кнопка 4', self)
        self.button4.clicked.connect(self.on_button4_clicked)
        self.buttons_layout.addWidget(self.button4)

        self.button5 = QPushButton('Кнопка 5', self)
        self.button5.clicked.connect(self.on_button5_clicked)
        self.buttons_layout.addWidget(self.button5)

        self.button6 = QPushButton('Кнопка 6', self)
        self.button6.clicked.connect(self.on_button6_clicked)
        self.buttons_layout.addWidget(self.button6)

        self.button7 = QPushButton('Кнопка 7', self)
        self.button7.clicked.connect(self.on_button7_clicked)
        self.buttons_layout.addWidget(self.button7)

        self.button8 = QPushButton('Кнопка 8', self)
        self.button8.clicked.connect(self.on_button8_clicked)
        self.buttons_layout.addWidget(self.button8)

        # Макет для правой части
        self.right_layout = QVBoxLayout()

        # Кнопка для открытия другого окна
        self.open_window_button = QPushButton('Открыть окно', self)
        self.open_window_button.clicked.connect(self.open_new_window)
        self.right_layout.addWidget(self.open_window_button)

        # Место для изображения OpenCV
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap('path_to_opencv_image.jpg'))  # Замените на путь к вашему изображению
        self.right_layout.addWidget(self.image_label)

        # Добавление макета кнопок в основной макет
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.right_layout)

        # Настройки окна
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('PyQt5 Окно с Кнопками')
        self.show()

    # Обработчики событий для кнопок
    def on_button1_clicked(self):
        print('Нажата кнопка 1')

    def on_button2_clicked(self):
        print('Нажата кнопка 2')

    def on_button3_clicked(self):
        print('Нажата кнопка 3')

    def on_button4_clicked(self):
        print('Нажата кнопка 4')

    def on_button5_clicked(self):
        print('Нажата кнопка 5')

    def on_button6_clicked(self):
        print('Нажата кнопка 6')

    def on_button7_clicked(self):
        print('Нажата кнопка 7')

    def on_button8_clicked(self):
        print('Нажата кнопка 8')


    def open_new_window(self):
        print("открыто окно")


# Запуск приложения