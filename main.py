import os
import cv2
from utils import detect_face_and_eyes, analyze_exposure, evaluate_image

# Папка с изображениями
images_folder = "images"

# Списки для результатов
good_images = []
average_images = []
bad_images = []

# Проходим по файлам в папке
for filename in os.listdir(images_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        filepath = os.path.join(images_folder, filename)
        image = cv2.imread(filepath)
        if image is None:
            continue

        # Детектируем лицо и глаза
        face_data = detect_face_and_eyes(image)
        # Анализ экспозиции
        mean_brightness = analyze_exposure(image)
        # Оцениваем изображение
        rating = evaluate_image(image, face_data, mean_brightness)
        
        # Выводим информацию
        print(f"{filename}: {rating} (средняя яркость: {mean_brightness:.1f}, найдено лиц: {len(face_data)})")
        
        if rating == "хорошая":
            good_images.append(filename)
        elif rating == "средняя":
            average_images.append(filename)
        else:
            bad_images.append(filename)

print("\nХорошие фотографии:")
print("\n".join(good_images))
print("\nСредние фотографии:")
print("\n".join(average_images))
print("\nПлохие фотографии:")
print("\n".join(bad_images))
