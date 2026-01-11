import cv2
import numpy as np

def crack_severity(screen_img):
    gray = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    crack_pixels = np.sum(edges > 0)
    total_pixels = edges.size

    return crack_pixels / total_pixels


def normalize_crack_score(raw_score):
    if raw_score < 0.01:
        return 0.05
    elif raw_score < 0.03:
        return 0.3
    elif raw_score < 0.06:
        return 0.6
    else:
        return 0.9
