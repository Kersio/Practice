from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QDialog, QLineEdit, QMessageBox)

import images


class MainWindow(QMainWindow):
    def __init__(self, prev_window, frame):
        super().__init__()
        self.init_ui()
        self.frame = frame
        self.prevWindow = prev_window

    def init_ui(self):
        # Основной виджет и макеты
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Макет для кнопок слева
        self.buttons_layout = QVBoxLayout()

        # Создание и добавление кнопок
        button_style = ("""
             QPushButton {
                 background-color: #4CAF50; 
                 border-style: solid;
                 border-radius: 30px;  /* Половина высоты */
                 border-width: 2px;
                 border-color: #008080;
                 font: bold 14px;
                 min-width: 60px;
                 min-height: 60px;  /* Делаем кнопку квадратной */
             }
             QPushButton:pressed {
                 background-color: #66BB6A;
             }
         """)
        self.button1 = QPushButton('Показать изображение', self)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.buttons_layout.addWidget(self.button1)
        self.button1.setStyleSheet(button_style)

        self.button2 = QPushButton('Показать красный канал изображения', self)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.buttons_layout.addWidget(self.button2)
        self.button2.setStyleSheet(button_style)

        self.button3 = QPushButton('Показать зеленый канал изображения', self)
        self.button3.clicked.connect(self.on_button3_clicked)
        self.buttons_layout.addWidget(self.button3)
        self.button3.setStyleSheet(button_style)

        self.button4 = QPushButton('Показать синий канал изображения', self)
        self.button4.clicked.connect(self.on_button4_clicked)
        self.buttons_layout.addWidget(self.button4)
        self.button4.setStyleSheet(button_style)

        self.button5 = QPushButton('Показать негативное изображение', self)
        self.button5.clicked.connect(self.on_button5_clicked)
        self.buttons_layout.addWidget(self.button5)
        self.button5.setStyleSheet(button_style)

        self.button6 = QPushButton('Добавить границы к изображению', self)
        self.button6.clicked.connect(self.on_button6_clicked)
        self.buttons_layout.addWidget(self.button6)
        self.button6.setStyleSheet(button_style)

        self.button7 = QPushButton('Нарисовать зеленую линию на изображении', self)
        self.button7.clicked.connect(self.on_button7_clicked)
        self.buttons_layout.addWidget(self.button7)
        self.button7.setStyleSheet(button_style)

        # Макет для правой части
        self.right_layout = QVBoxLayout()

        # Кнопка для открытия другого окна
        self.open_window_button = QPushButton('Вернуться к выбору изображения', self)
        self.open_window_button.clicked.connect(self.open_menu_window)
        self.right_layout.addWidget(self.open_window_button)
        self.open_window_button.setStyleSheet(button_style)

        # Место для изображения OpenCV
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap('Picture2.jpg'))
        self.image_label.setMaximumSize(1440, 810)
        self.right_layout.addWidget(self.image_label)

        # Добавление макета кнопок в основной макет
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.right_layout)

        # Настройки окна
        self.showMaximized()  # Отображение окна в максимизированном режиме с рамками
        self.setWindowTitle('Обработка изображения')
        self.show()

    # Обработчики событий для кнопок
    def on_button1_clicked(self):
        images.convert_image_to_jpg(self.frame)
        self.image_label.setPixmap(QPixmap("output_image.jpg"))

    def on_button2_clicked(self):
        images.convert_image_to_jpg(images.image_channel(self.frame, "R"))
        self.image_label.setPixmap(QPixmap("output_image.jpg"))

    def on_button3_clicked(self):
        images.convert_image_to_jpg(images.image_channel(self.frame, "G"))
        self.image_label.setPixmap(QPixmap("output_image.jpg"))

    def on_button4_clicked(self):
        images.convert_image_to_jpg(images.image_channel(self.frame, "B"))
        self.image_label.setPixmap(QPixmap("output_image.jpg"))

    def on_button5_clicked(self):
        images.convert_image_to_jpg(images.negative_image(self.frame))
        self.image_label.setPixmap(QPixmap("output_image.jpg"))

    def on_button6_clicked(self):
        self.dialog_border = BorderDialog(self, self.frame)
        self.hide()
        self.dialog_border.show()

    def on_button7_clicked(self):
        self.dialog_line = LineDialog(self, self.frame)
        self.hide()
        self.dialog_line.show()

    def open_menu_window(self):
        self.close()
        self.prevWindow.show()


class BorderDialog(QDialog):
    def __init__(self, prev_window, frame):
        super().__init__()
        self.prev_window = prev_window
        self.frame = frame
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Введите значения')

        # Создание меток и полей для ввода
        self.right_input = QLineEdit(self)
        self.left_input = QLineEdit(self)
        self.top_input = QLineEdit(self)
        self.bottom_input = QLineEdit(self)

        # Кнопка для сохранения значений
        button_style = ("""
             QPushButton {
                 background-color: #4CAF50; 
                 border-style: solid;
                 border-radius: 30px;  /* Половина высоты */
                 border-width: 2px;
                 border-color: #008080;
                 font: bold 14px;
                 min-width: 30px;
                 min-height: 30px;  /* Делаем кнопку квадратной */
             }
             QPushButton:pressed {
                 background-color: #66BB6A;
             }
         """)
        self.save_button = QPushButton('Сохранить', self)
        self.save_button.clicked.connect(self.save_values)
        self.save_button.setStyleSheet(button_style)

        layout = QVBoxLayout()

        layout.addWidget(QLabel('Right:'))
        layout.addWidget(self.right_input)

        layout.addWidget(QLabel('Left:'))
        layout.addWidget(self.left_input)

        layout.addWidget(QLabel('Top:'))
        layout.addWidget(self.top_input)

        layout.addWidget(QLabel('Bottom:'))
        layout.addWidget(self.bottom_input)

        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_values(self):
        if (
                self.right_input.text() == "" or self.top_input.text() == ""
                or self.left_input.text() == "" or self.bottom_input.text() == ""
        ) or not (
                self.right_input.text().isdigit() or self.top_input.text().isdigit()
                or self.left_input.text().isdigit() or self.bottom_input.text().isdigit()
        ):
            self.close()
            self.error_input()
        else:
            # Сохранение значений из полей ввода в переменные
            self.right_value = int(self.right_input.text())
            self.left_value = int(self.left_input.text())
            self.top_value = int(self.top_input.text())
            self.bottom_value = int(self.bottom_input.text())
            if (
                    self.top_value < 0 or self.bottom_value < 0
                    or self.left_value < 0 or self.right_value < 0
            ) or (
                    self.left_value + self.right_value > self.frame.shape[1]
                    or self.top_value + self.bottom_value > self.frame.shape[0]
            ):
                self.close()
                self.error_input()
            else:
                self.image_add_border()

    def image_add_border(self):
        images.convert_image_to_jpg(
            images.image_make_border(
                self.frame, self.top_value,
                self.bottom_value, self.left_value,
                self.right_value
            )
        )
        self.close()
        self.prev_window.image_label.setPixmap(QPixmap("output_image.jpg"))
        self.prev_window.show()

    def error_input(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка: введенные данные некорректны")
        msg.setInformativeText('Возврат к окну обработки изображения')
        msg.setWindowTitle("Ошибка ввода")
        msg.exec_()  # Отображение диалогового окна с ошибкой
        msg.raise_()

        self.prev_window.show()


class LineDialog(QWidget):
    def __init__(self, prev_window, frame):
        super().__init__()
        self.prev_window = prev_window
        self.frame = frame
        self.init_ui()

    def init_ui(self):
        # Создание подписей и полей ввода
        self.label_x1 = QLabel('x1', self)
        self.line1_input1 = QLineEdit(self)
        self.label_y1 = QLabel('y1', self)
        self.line1_input2 = QLineEdit(self)

        self.label_x2 = QLabel('x2', self)
        self.line2_input1 = QLineEdit(self)
        self.label_y2 = QLabel('y2', self)
        self.line2_input2 = QLineEdit(self)

        self.label_thickness = QLabel('Толщина линии', self)
        self.line3_input = QLineEdit(self)

        # Создание кнопки для сохранения данных
        button_style = ("""
             QPushButton {
                 background-color: #4CAF50; 
                 border-style: solid;
                 border-radius: 30px;  /* Половина высоты */
                 border-width: 2px;
                 border-color: #008080;
                 font: bold 14px;
                 min-width: 30px;
                 min-height: 30px;  /* Делаем кнопку квадратной */
             }
             QPushButton:pressed {
                 background-color: #66BB6A;
             }
         """)
        self.save_button = QPushButton('Сохранить', self)
        self.save_button.clicked.connect(self.saveData)
        self.save_button.setStyleSheet(button_style)

        # Создание горизонтальных макетов с подписями и полями ввода
        line1_layout = QHBoxLayout()
        line1_layout.addWidget(self.label_x1)
        line1_layout.addWidget(self.line1_input1)
        line1_layout.addWidget(self.label_y1)
        line1_layout.addWidget(self.line1_input2)

        line2_layout = QHBoxLayout()
        line2_layout.addWidget(self.label_x2)
        line2_layout.addWidget(self.line2_input1)
        line2_layout.addWidget(self.label_y2)
        line2_layout.addWidget(self.line2_input2)

        line3_layout = QHBoxLayout()
        line3_layout.addWidget(self.label_thickness)
        line3_layout.addWidget(self.line3_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(line1_layout)
        main_layout.addLayout(line2_layout)
        main_layout.addLayout(line3_layout)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def saveData(self):
        if not (
                self.line1_input1.text().isdigit()
                or self.line1_input2.text().isdigit()
                or self.line2_input1.text().isdigit()
                or self.line2_input2.text().isdigit()
                or self.line3_input.text().isdigit()
        ):
            self.close()
            self.error_input()
        else:
            self.x1_value = int(self.line1_input1.text())
            self.y1_value = int(self.line1_input2.text())
            self.x2_value = int(self.line2_input1.text())
            self.y2_value = int(self.line2_input2.text())
            self.thickness_value = int(self.line3_input.text())

            if (
                    self.x1_value == ""
                    or self.x2_value == "" or self.y1_value == ""
                    or self.y2_value == "" or self.thickness_value == ""
            ):
                self.close()
                self.error_input()

            if (
                    self.x1_value < 0 or self.y1_value < 0
                    or self.x2_value < 0 or self.y2_value < 0
                    or self.thickness_value <= 0
            ) or (
                    self.x1_value > self.x2_value or self.y1_value > self.y2_value
            ) or self.thickness_value >= 32000 \
                    or (
                    self.x1_value > self.frame.shape[1]
                    or self.x2_value > self.frame.shape[1]
                    or self.y1_value > self.frame.shape[0]
                    or self.y2_value > self.frame.shape[0]
            ):
                self.close()
                self.error_input()

            else:
                self.draw_line()

    def error_input(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка: введенные данные некорректны")
        msg.setInformativeText('Возврат к окну обработки изображения')
        msg.setWindowTitle("Ошибка ввода")
        msg.exec_()  # Отображение диалогового окна с ошибкой
        msg.raise_()

        self.prev_window.show()

    def draw_line(self):
        images.convert_image_to_jpg(
            images.image_add_green_line(
                self.frame, self.x1_value,
                self.y1_value, self.x2_value,
                self.y2_value, self.thickness_value
            )
        )
        self.close()
        self.prev_window.image_label.setPixmap(QPixmap("output_image.jpg"))
        self.prev_window.show()
