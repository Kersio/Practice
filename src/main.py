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