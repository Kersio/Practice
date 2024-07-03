import cv2
import numpy
import numpy as np


# Получить изображение путем к файлу
def get_file_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is not (None):
        return image
    else:
        print("скибиди доп доп ес ес")


# Проверка доступности камеры по индексу
def check_camera(index: int) -> bool:
    cap = cv2.VideoCapture(index)
    if cap is None or not cap.isOpened():
        return False
    cap.release()
    return True


"""
# Перебор индексов камер и возвращение доступных
def list_available_cameras(max_index=10):
    available_cameras = []
    for i in range(max_index):
        if check_camera(i):
            available_cameras.append(i)
    return available_cameras
"""


# Получение изображения с веб-камеры
def get_camera_image(index: int) -> numpy.ndarray:
    cap = cv2.VideoCapture(index)
    ret, frame = cap.read()
    if ret:
        cap.release()
        return frame
    else:
        print("не получилось получить изображение с указанной веб-камеры")

# Выводит изображение окном OpenCV
def show_camera_image(frame: numpy.ndarray):
    cv2.imshow(
        "a", frame
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# добавляет границу к изображению
def image_make_border(frame: numpy.ndarray, top: int,
                      bottom: int, left: int,
                      right: int) -> numpy.ndarray:
    return cv2.copyMakeBorder(
        frame, top,
        bottom, left,
        right, borderType=cv2.BORDER_CONSTANT,
        value=0
    )


# рисует зеленую линию на изображении
def image_add_green_line(frame: numpy.ndarray, x1: int, y1: int, x2: int, y2: int, thickness: int):
    return cv2.line(
        frame, (x1, y1),
        (x2, y2), (0, 255, 0),
        thickness
    )

#cv2.bitwise_not(frame) негативное изображение
