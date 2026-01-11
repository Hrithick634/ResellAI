def calculate_resale_price(mrp, x, y):
    

    resale_fraction = (
        0.2 + 
        0.3 * (x)
        + 0.5 * (1 - y)
    )

    resale_fraction = min(resale_fraction, 1.0)
    return round(resale_fraction * mrp, 2)
