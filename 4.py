import math

def target(x: float, y: float) -> Union[int, str]:
    distance = math.sqrt(x2 + y2)
    for radius in range(1, 11):
        if distance <= radius:
            return radius
    return "missed"
