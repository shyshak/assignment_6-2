def celcius_to_fahrenheit(cel: float) -> float:
    return round((9/5 * cel + 32), 2)


def fahrenheit_to_celcius(far: float) -> float:
    return round((5/9 * (far - 32)), 2)
