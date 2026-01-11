from fastapi import APIRouter, UploadFile, File, Form

from app.services.yolo_service import detect_screen
from app.services.pricing_service import calculate_resale_price
from app.utils.image_utils import save_upload
from app.services.ml_service import predict_spec_depreciation
from app.utils.brand_utils import encode_brand
from app.services.cnn_service import predict_damage_from_image




router = APIRouter()

@router.post("/predict")
def predict_damage(
    file: UploadFile = File(...),
    mrp: float = Form(...),
    ram: int = Form(...),
    storage: int = Form(...),
    phone_age: int = Form(...),      # age bucket: 1–6
    backbody: int = Form(...), 
    brand: str = Form(...)
):
    image_path = save_upload(file)

    screen = detect_screen(image_path)
    if screen is None:
        return {
            "screen_detected": False,
            "resale_value": None
        }

    cnn_result = predict_damage_from_image(image_path)

    y = cnn_result["damage_score"]



    brand_encoding = encode_brand(brand)

    features = [
        ram,
        storage,
        phone_age,
        backbody,
        brand_encoding["Brand_Oneplus"],
        brand_encoding["Brand_Redmi"],
        brand_encoding["Brand_Samsung"],
        brand_encoding["Brand_Xiaomi"],
    ]

    x = predict_spec_depreciation(features)
    


    resale_price = calculate_resale_price(mrp, x, y)

    return {
    "screen_detected": True,
    "damage_score": y,
    "damage_class": cnn_result["predicted_class"],
    "spec_depreciation": round(1 - x, 2),
    "resale_value": resale_price
}
