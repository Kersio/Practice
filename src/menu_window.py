import os

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QVBoxLayout, QMessageBox

import images


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

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

        button1 = QPushButton('Получить изображение с веб-камеры', self)
        button2 = QPushButton('Выбрать изображение', self)
        button1.clicked.connect(self.camera)
        button2.clicked.connect(self.file_image)
        button1.setStyleSheet(button_style)
        button2.setStyleSheet(button_style)

        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        self.setLayout(vbox)
        self.setFixedSize(400, 280)

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
            self.close()
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