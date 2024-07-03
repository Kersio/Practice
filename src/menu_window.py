import os

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QVBoxLayout, QMessageBox
import images
import main_window


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

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

        self.setWindowTitle('Выбор изображения')
        self.show()

    def camera(self):
        self.close()
        if images.check_camera(0):
            self.frame = images.get_camera_image(0)
            self.mainWindow = main_window.MainWindow(self, self.frame)
            self.mainWindow.show()
        else:
            self.hide()
            self.error_camera()
    def file_image(self):
        file_path = QFileDialog.getOpenFileName(
            self, caption="Выбрать PNG файл",
            directory="", filter="JPG Files (*.jpg);;PNG Files (*.png)"
        )[0]
        # Проверка указанного пути на валидность
        if os.path.exists(file_path) and os.path.isfile(file_path):
            self.close()
            self.frame = images.get_file_image(file_path)
            self.mainWindow = main_window.MainWindow(self, self.frame)
            self.mainWindow.show()
        else:
            self.hide()
            self.error_path_file()

    def error_path_file(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка: выбранный файл невалиден")
        msg.setInformativeText('Пожалуйста, выберите другой файл')
        msg.setWindowTitle("Ошибка")
        msg.exec_()  # Отображение диалогового окна с ошибкой
        msg.raise_()

        self.show()

    def error_camera(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка: нет подключенных веб-камер")
        msg.setInformativeText('Можно решить проблему следующим образом:\n'
                               '- проверить соединение кабеля камеры,\n'
                               '- выбрать другой способ загрузки изображения,\n'
                               '- проверить наличие драйверов '
                               '(обновить их если они старые).')
        msg.setWindowTitle("Ошибка")
        msg.exec_()  # Отображение диалогового окна с ошибкой
        msg.raise_()

        self.show()


app = QApplication([])
ex = MenuWindow()
app.exec_()
