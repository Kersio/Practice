import cv2
import numpy


# Получить изображение путем к файлу
def get_file_image(path: str) -> numpy.ndarray:
    file = open(path, "rb")
    bytes = bytearray(file.read())
    numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
    image = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    return image


# Проверка доступности камеры по индексу
def check_camera(index: int) -> bool:
    try:
        cap = cv2.VideoCapture(index)
        if cap is None or not cap.isOpened():
            raise
    except :
        return False
    cap.release()
    return True


# Получение изображения с веб-камеры
def get_camera_image(index: int) -> numpy.ndarray:
    cap = cv2.VideoCapture(index)
    ret, frame = cap.read()
    cap.release()
    return frame


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
        value=2555
    )


# рисует зеленую линию на изображении
def image_add_green_line(frame: numpy.ndarray, x1: int, y1: int, x2: int, y2: int, thickness: int):
    return cv2.line(
        frame, (x1, y1),
        (x2, y2), (0, 255, 0),
        thickness
    )


def negative_image(frame: numpy.ndarray) -> numpy.ndarray:
    return cv2.bitwise_not(frame)


def convert_image_to_jpg(frame):
    cv2.imwrite('./res/output_image.jpg', frame)


def image_channel(frame, color):
    # Разделение на цветовые каналы
    b, g, r = cv2.split(frame)

    if color == "R":
        return cv2.merge([numpy.zeros_like(b), numpy.zeros_like(g), r])

    elif color == "G":
        return cv2.merge([numpy.zeros_like(b), g, numpy.zeros_like(r)])

    return cv2.merge([b, numpy.zeros_like(g), numpy.zeros_like(r)])
