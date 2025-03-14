import os
import cv2
from utils import detect_face_and_eyes, analyze_exposure, evaluate_image

images_folder = "images"

good_images = []
average_images = []
bad_images = []

for filename in os.listdir(images_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        filepath = os.path.join(images_folder, filename)
        image = cv2.imread(filepath)
        if image is None:
            continue

        face_data = detect_face_and_eyes(image)
        mean_brightness = analyze_exposure(image)
        rating = evaluate_image(image, face_data, mean_brightness)
        
        print(f"{filename}: {rating} (average brightness: {mean_brightness:.1f}, found faces: {len(face_data)})")
        
        if rating == "good":
            good_images.append(filename)
        elif rating == "average":
            average_images.append(filename)
        else:
            bad_images.append(filename)

print("\nGood photos:")
print("\n".join(good_images))
print("\nAverage photos:")
print("\n".join(average_images))
print("\nBad photos:")
print("\n".join(bad_images))
