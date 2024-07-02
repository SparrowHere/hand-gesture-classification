import os
import cv2
import math
import pickle
import time
import numpy as np
import warnings
import mediapipe as mp

warnings.filterwarnings("ignore")

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480
CLASS = ["Open Palm", "Peace Sign", "Rock On", "OK Sign","NOK Sign"]
CLASS_IDX = 0
COUNT = 0
TOTAL = 100
MODEL_DIR = os.getcwd() + "\\models\\hand_gesture_model.pkl"

HANDS = mp.solutions.hands.Hands(
    model_complexity=1,
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5,
    )
DRAW = mp.solutions.drawing_utils

MODEL = pickle.load(open(MODEL_DIR, 'rb'))
CAP = cv2.VideoCapture(0)

def resize(image, DESIRED_HEIGHT, DESIRED_WIDTH):
    """
    Resizes the given image while maintaining the aspect ratio.

    Args:
        image (`np.ndarray`): The input image to be resized.
        desired_height (`int`): The desired height of the output image.
        desired_width (`int`): The desired width of the output image.

    Returns:
        `np.ndarray`: The resized image.
    """
    H, W = image.shape[:2]
    if H < W:       # Portrait
        image = cv2.resize(image, (DESIRED_WIDTH, math.floor(H / (W / DESIRED_WIDTH))))
    else:
        image = cv2.resize(image, (math.floor(W / (H / DESIRED_HEIGHT)), DESIRED_HEIGHT))
    return image

def main():
    """
    Captures real-time video from the webcam, processes each frame to detect hand landmarks,
    and classifies the hand gesture based on the detected landmarks.
    """
    while CAP.isOpened():
        ret, frame = CAP.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue

        frame = resize(frame, DESIRED_HEIGHT, DESIRED_WIDTH)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = HANDS.process(frame_rgb)
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            landmarks = np.array([[landmark.x, landmark.y, landmark.z] for landmark in hand_landmarks.landmark]).flatten()
            prediction = MODEL.predict([landmarks])
            DRAW.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            x_min = int(min(landmark.x for landmark in hand_landmarks.landmark) * frame.shape[1])
            y_min = int(min(landmark.y for landmark in hand_landmarks.landmark) * frame.shape[0])
            x_max = int(max(landmark.x for landmark in hand_landmarks.landmark) * frame.shape[1])
            y_max = int(max(landmark.y for landmark in hand_landmarks.landmark) * frame.shape[0])

            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            label_x = x_min
            label_y = y_min - 10

            cv2.putText(frame, CLASS[int(prediction)], (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('MediaPipe Hands', frame)

        if cv2.waitKey(5) & 0xFF == ord('s'):
            img_name = os.path.join(os.getcwd() + "\\test", f"test_{time.time()}.jpg")
            cv2.imwrite(img_name, frame)
            print(f"Saved frame as '{img_name}'")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    CAP.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()