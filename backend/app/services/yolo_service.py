from ultralytics import YOLO
import cv2

from app.config import YOLO_MODEL_PATH, CONF_THRESHOLD

yolo_model = YOLO(YOLO_MODEL_PATH)

def detect_screen(image_path):
    results = yolo_model(image_path, conf=CONF_THRESHOLD)

    for r in results:
        if r.boxes is None or len(r.boxes) == 0:
            return None

        box = r.boxes.xyxy[0]
        x1, y1, x2, y2 = map(int, box)

        img = cv2.imread(image_path)
        crop = img[y1:y2, x1:x2]

        return crop

    return None
