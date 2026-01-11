import os
import gdown

os.makedirs("models", exist_ok=True)

files = {
    "cnn_damage_model_tf2.h5": "https://drive.google.com/file/d/1LO0bjC-oujBTowRpIQMyl_PheLY3BOMq/view?usp=sharing",
    "best.pt": "https://drive.google.com/file/d/1y--WNg8yKT_OExMZjsy2mYC5VWH_sbve/view?usp=sharing",
    "xgboost_resale_model.pkl": "https://drive.google.com/file/d/134d4T6a0vfwEQQJRoJD4gw9YeUZRuYnx/view?usp=sharing"
}

for filename, url in files.items():
    path = os.path.join("models", filename)
    if not os.path.exists(path):
        print(f"Downloading {filename}...")
        gdown.download(url, path, quiet=False)
    else:
        print(f"{filename} already exists")
