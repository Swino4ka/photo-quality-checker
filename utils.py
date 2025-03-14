import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_default.xml")
eye_cascade  = cv2.CascadeClassifier("classifiers/haarcascade_eye.xml")

def detect_face_and_eyes(image):
    """
    Detects a face and eyes in an image.
    Returns a list of faces, where for each face it returns (x, y, w, h) and a list of eyes (each eye: (ex, ey, ew, eh))
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
    Analyzes the exposure of an image.
    Returns the average brightness value (0-255) for the entire image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # The average brightness is calculated as the mean value of all pixels in the image
    mean_val = np.mean(gray)
    return mean_val

def evaluate_image(image, face_data, mean_brightness,
                   brightness_good=(80, 170)):
    """
    Evaluates an image by three parameters:
       - Presence of a face (face_data is not empty)
       - Presence of 2 eyes (on the first found face)
       - Average brightness within the acceptable range (brightness_good)
    Returns a rating: "good", "average", "bad"
    """
    if len(face_data) == 0:
        return "плохая"
    
    # Evaluates the presence of eyes in the first person (can be improved for several persons)
    eyes = face_data[0]["eyes"]
    if len(eyes) < 2:
        eye_status = False
    else:
        eye_status = True

    # Evaluates the average brightness of the image
    if brightness_good[0] <= mean_brightness <= brightness_good[1]:
        exposure_status = True
    else:
        exposure_status = False

    # Returns the final rating
    if eye_status and exposure_status:
        return "good"
    elif not eye_status and not exposure_status:
        return "bad"
    else:
        return "average"
