import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

# ======================================================
# CONFIG
# ======================================================

MODEL_PATH = "/Users/hrithickkanagaraj/Documents/Programming /ML/Damage_classification/CNN/cnn_damage_model_tf2.h5"
IMAGE_SIZE = (224, 224)

CLASS_NAMES = [
    "light_broken",
    "moderately_broken",
    "no_broken",
    "severe_broken"
]

# Weighted damage severity (used to compute y)
DAMAGE_WEIGHTS = {
    "no_broken": 0.0,
    "light_broken": 0.3,
    "moderately_broken": 0.6,
    "severe_broken": 1.0
}

# ======================================================
# LOAD MODEL (ONCE AT STARTUP)
# ======================================================

print("🔍 Checking CNN model path...")
print(MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"❌ CNN MODEL FILE NOT FOUND: {MODEL_PATH}")

print("🔄 Loading CNN model...")
model = load_model(MODEL_PATH, compile=False)
print("✅ CNN MODEL LOADED SUCCESSFULLY")

# ======================================================
# PREDICTION FUNCTION
# ======================================================

def predict_damage_from_image(image_path: str):
    """
    Input  : image file path
    Output : {
        predicted_class,
        damage_score (0–1),
        probabilities
    }
    """

    if not os.path.exists(image_path):
        raise RuntimeError(f"❌ IMAGE NOT FOUND: {image_path}")

    # Load + preprocess image
    img = load_img(image_path, target_size=IMAGE_SIZE)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict
    probs = model.predict(x, verbose=0)[0]

    predicted_idx = int(np.argmax(probs))
    predicted_class = CLASS_NAMES[predicted_idx]

    # Convert softmax → severity score
    damage_score = sum(
        probs[i] * DAMAGE_WEIGHTS[CLASS_NAMES[i]]
        for i in range(len(CLASS_NAMES))
    )

    return {
        "predicted_class": predicted_class,
        "damage_score": round(float(damage_score), 3),
        "probabilities": [round(float(p), 4) for p in probs]
    }
