import cv2
import numpy


# Получить изображение путем к файлу
def get_file_image(path: str) -> numpy.ndarray:
    """
    Получает изображение из файла по указанному пути

    :param path: Путь к файлу изображения
    :return: Изображение в виде массива numpy
    """
    file = open(path, "rb")
    bytes = bytearray(file.read())
    numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
    image = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    return image


def check_camera(index: int) -> bool:
    """
    Проверяет доступность камеры по индексу

    :param index: Индекс камеры
    :return: True, если камера доступна, иначе False
    """
    cap = cv2.VideoCapture(index)
    if cap is None or not cap.isOpened():
        return False
    cap.release()
    return True


def get_camera_image(index: int) -> numpy.ndarray:
    """
    Получает изображение с веб-камеры по индексу

    :param index: Индекс камеры
    :return: Изображение в виде массива numpy
    """
    cap = cv2.VideoCapture(index)
    ret, frame = cap.read()
    cap.release()
    return frame


def show_camera_image(frame: numpy.ndarray):
    """
    Отображает изображение в окне OpenCV

    :param frame: Изображение для отображения
    """
    cv2.imshow(
        "a", frame
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_make_border(frame: numpy.ndarray, top: int,
                      bottom: int, left: int,
                      right: int) -> numpy.ndarray:
    """
    Добавляет границу к изображению

    :param frame: Исходное изображение
    :param top: Ширина границы сверху
    :param bottom: Ширина границы снизу
    :param left: Ширина границы слева
    :param right: Ширина границы справа
    :return: Изображение с границей
    """
    return cv2.copyMakeBorder(
        frame, top,
        bottom, left,
        right, borderType=cv2.BORDER_CONSTANT,
        value=2555
    )


def image_add_green_line(frame: numpy.ndarray, x1: int, y1: int, x2: int, y2: int, thickness: int):
    """
    Рисует зеленую линию на изображении.

    :param frame: Исходное изображение.
    :param x1: Начальная координата оси x линии.
    :param y1: Начальная координата оси y линии.
    :param x2: Конечная координата оси x линии.
    :param y2: Конечная координата оси y линии.
    :param thickness: Толщина линии.
    :return: Изображение с зеленой линией.
    """
    return cv2.line(
        frame, (x1, y1),
        (x2, y2), (0, 255, 0),
        thickness
    )


def negative_image(frame: numpy.ndarray) -> numpy.ndarray:
    """
    Создает негативное изображения

    :param frame: Исходное изображение
    :return: Негатив изображения
    """
    return cv2.bitwise_not(frame)


def convert_image_to_jpg(frame):
    """
    Конвертирует и сохраняет изображение в формате JPG по пути ./res/output_image.jgp

    :param frame: Исходное изображение
    """
    cv2.imwrite('./res/output_image.jpg', frame)


def image_channel(frame, color):
    """
    Возвращает изображение с выделенным цветовым каналом.

    :param frame: Исходное изображение
    :param color: Цветовой канал для выделения ('R', 'G', 'B')
    :return: Изображение с выделенным цветовым каналом
    """
    # Разделение на цветовые каналы
    b, g, r = cv2.split(frame)

    if color == "R":
        return cv2.merge([numpy.zeros_like(b), numpy.zeros_like(g), r])

    elif color == "G":
        return cv2.merge([numpy.zeros_like(b), g, numpy.zeros_like(r)])

    return cv2.merge([b, numpy.zeros_like(g), numpy.zeros_like(r)])
