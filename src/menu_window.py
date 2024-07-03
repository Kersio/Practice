import os

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QVBoxLayout, QMessageBox

import images


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setFixedSize(400, 300)

        button1 = QPushButton('Получить изображение с веб-камеры', self)
        button2 = QPushButton('Выбрать изображение', self)
        button1.clicked.connect(self.camera)
        button2.clicked.connect(self.file_image)

        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        self.setLayout(vbox)

        # Настройки окна
        self.setWindowTitle('Practice')
        self.show()

    def camera(self):
        self.close()
        images.get_camera_image(0)

    def file_image(self):
        filePath = QFileDialog.getOpenFileName(
            self, caption= "Выбрать PNG файл",
            directory="", filter="JPG Files (*.jpg);;PNG Files (*.png)"
        )[0]

        # Проверка указанного пути на валидность
        if os.path.exists(filePath) and os.path.isfile(filePath):
            pass
        else:
            self.close()
            self.error_path_file()

    def error_path_file(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка: выбранный файл невалиден")
        msg.setInformativeText('Пожалуйста, выберите другой файл')
        msg.setWindowTitle("Ошибка")
        msg.exec_()  # Отображение диалогового окна с ошибкой

        self.show()


app = QApplication([])
ex = MenuWindow()
app.exec_()

"""
from PyQt5.QtWidgets import QApplication, QFileDialog


def open_file_dialog():
    app = QApplication([])
    # Вызов диалога выбора файла
    file_path = QFileDialog.getOpenFileName(
        caption='Выберите изображение',
        filter='PNG images (*.png)'
    )

    if file_path:
        print(f'Выбран файл: {file_path}')
    else:
        print('Файл не выбран.')

    return file_path


# Вызов функции для открытия диалога выбора файла
selected_file = open_file_dialog()
print(selected_file)
"""