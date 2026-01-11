def encode_brand(brand: str):
    """
    One-hot encode brand.
    Apple is the reference category (all zeros).
    """
    brand = brand.lower()

    return {
        "Brand_Oneplus": 1 if brand == "oneplus" else 0,
        "Brand_Redmi": 1 if brand == "redmi" else 0,
        "Brand_Samsung": 1 if brand == "samsung" else 0,
        "Brand_Xiaomi": 1 if brand == "xiaomi" else 0,
    }
