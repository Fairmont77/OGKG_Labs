# 1. Локалізація точки на планарному розбитті методом трапецій.

class Trapezoid:

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def contains_point(self, x, y):
        return self.left <= x <= self.right and self.bottom <= y <= self.top


def locate_point(trapezoids, point):
    x, y = point
    for trapezoid in trapezoids:
        if trapezoid.contains_point(x, y):
            return trapezoid
    return None


# cтворення декількох трапецій і тестування точки
trapezoids = [
    Trapezoid(1, 5.5, 10.1, 0),
    Trapezoid(6, 11.2, 10, 0),
]

# Точка, яку треба локалізувати
point = (3, 5)

# Знаходимо, у якій трапеції знаходиться точка
located_trapezoid = locate_point(trapezoids, point)

if located_trapezoid:
    print(
        f"Точка знаходиться в трапеції з границями {located_trapezoid.left}, {located_trapezoid.right}, {located_trapezoid.top}, {located_trapezoid.bottom}.")
else:
    print("Точка не знаходиться в жодній трапеції.")
