import cv2
import numpy as np

# Загружаем каскады (укажите путь к файлам XML в папке classifiers)
face_cascade = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_default.xml")
eye_cascade  = cv2.CascadeClassifier("classifiers/haarcascade_eye.xml")

def detect_face_and_eyes(image):
    """
    Детектирует лицо и глаза на изображении.
    Возвращает список лиц, где для каждого лица возвращается (x, y, w, h) и список глаз (каждый глаз: (ex, ey, ew, eh))
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    results = []
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi)
        results.append({"face": (x, y, w, h), "eyes": eyes})
    return results

def analyze_exposure(image):
    """
    Анализирует экспозицию изображения.
    Возвращает среднее значение яркости (0-255) для всего изображения.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Рассчитаем среднее значение яркости
    mean_val = np.mean(gray)
    return mean_val

def evaluate_image(image, face_data, mean_brightness,
                   brightness_good=(80, 170)):
    """
    Оценивает изображение по трем параметрам:
      - Наличие лица (face_data не пустое)
      - Наличие 2 глаз (на первом найденном лице)
      - Средняя яркость внутри допустимого диапазона (brightness_good)
    Возвращает оценку: "хорошая", "средняя", "плохая"
    """
    # Если лица не обнаружены, сразу плохая оценка
    if len(face_data) == 0:
        return "плохая"
    
    # Оценим наличие глаз у первого лица (можно доработать для нескольких лиц)
    eyes = face_data[0]["eyes"]
    if len(eyes) < 2:
        eye_status = False
    else:
        eye_status = True

    # Оценим экспозицию
    if brightness_good[0] <= mean_brightness <= brightness_good[1]:
        exposure_status = True
    else:
        exposure_status = False

    # Простой алгоритм оценки:
    if eye_status and exposure_status:
        return "хорошая"
    elif not eye_status and not exposure_status:
        return "плохая"
    else:
        return "средняя"
