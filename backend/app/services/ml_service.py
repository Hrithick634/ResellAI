import pickle
import numpy as np

MODEL_PATH = "/Users/hrithickkanagaraj/Documents/Programming /ML/Damage_classification/ML/xgboost_resale_model.pkl"

with open(MODEL_PATH, "rb") as f:
    xgb_model = pickle.load(f)


def predict_spec_depreciation(features):
    """
    features = [Ram, Storage, Phone_age, Body_broken,
                Brand_Oneplus, Brand_Redmi, Brand_Samsung, Brand_Xiaomi]
    """
    features = np.array(features).reshape(1, -1)

    x = xgb_model.predict(features)[0]

    # safety clamp
    x = float(np.clip(x, 0.0, 1.0))
    return x
