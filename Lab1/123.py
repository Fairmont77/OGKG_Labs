import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Segment(({self.p1.x}, {self.p1.y}), ({self.p2.x}, {self.p2.y}))"

class Trapezoid:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def __str__(self):
        return f"Trapezoid(left={self.left}, right={self.right}, bottom={self.bottom}, top={self.top})"

class TrapezoidalMap:
    def __init__(self, segments):
        self.segments = segments
        self.trapezoids = []

    def build(self):
        initial_trapezoid = Trapezoid(float('inf'), -float('inf'), float('-inf'), float('inf'))
        self.trapezoids.append(initial_trapezoid)
        for segment in self.segments:
            self.add_segment(segment)

    def add_segment(self, segment):
        new_trapezoids = []
        for trapezoid in self.trapezoids:
            if self.intersects(trapezoid, segment):
                new_trapezoids.extend(self.split_trapezoid(trapezoid, segment))
            else:
                new_trapezoids.append(trapezoid)
        self.trapezoids = new_trapezoids

    def intersects(self, trapezoid, segment):
        return not (segment.p1.x > trapezoid.right or segment.p2.x < trapezoid.left or
                    segment.p1.y > trapezoid.top or segment.p2.y < trapezoid.bottom)

    def split_trapezoid(self, trapezoid, segment):
        # Split the trapezoid into smaller trapezoids based on the segment
        if segment.p1.x == segment.p2.x:
            left_trapezoid = Trapezoid(trapezoid.top, trapezoid.bottom, trapezoid.left, segment.p1.x)
            right_trapezoid = Trapezoid(trapezoid.top, trapezoid.bottom, segment.p1.x, trapezoid.right)
            return [left_trapezoid, right_trapezoid]
        else:
            mid_x = (segment.p1.x + segment.p2.x) / 2
            left_trapezoid = Trapezoid(trapezoid.top, trapezoid.bottom, trapezoid.left, mid_x)
            right_trapezoid = Trapezoid(trapezoid.top, trapezoid.bottom, mid_x, trapezoid.right)
            top_trapezoid = Trapezoid(trapezoid.top, segment.p1.y, segment.p1.x, segment.p2.x)
            bottom_trapezoid = Trapezoid(segment.p1.y, trapezoid.bottom, segment.p1.x, segment.p2.x)
            return [left_trapezoid, right_trapezoid, top_trapezoid, bottom_trapezoid]

    def locate_point(self, point):
        for trapezoid in self.trapezoids:
            if trapezoid.left <= point.x <= trapezoid.right and trapezoid.bottom <= point.y <= trapezoid.top:
                return trapezoid
        return None

def plot_trapezoidal_map(trapezoidal_map, point=None):
    fig, ax = plt.subplots()
    for trapezoid in trapezoidal_map.trapezoids:
        if trapezoid.left != float('-inf') and trapezoid.right != float('inf'):
            rect = plt.Rectangle((trapezoid.left, trapezoid.bottom), trapezoid.right - trapezoid.left,
                                 trapezoid.top - trapezoid.bottom, edgecolor='blue', facecolor='none')
            ax.add_patch(rect)
    if point:
        plt.plot(point.x, point.y, 'ro')
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.show()

# Введення даних для відрізків
vertices = [
    Point(11, 2), Point(19, 4), Point(7, 7), Point(11, 7), Point(19, 11),
    Point(11, 12), Point(17, 14), Point(3, 15), Point(8, 19)
]

edges = [
    Segment(vertices[0], vertices[2]), Segment(vertices[0], vertices[3]), Segment(vertices[0], vertices[4]), Segment(vertices[0], vertices[1]),
    Segment(vertices[1], vertices[4]), Segment(vertices[2], vertices[3]), Segment(vertices[2], vertices[7]), Segment(vertices[2], vertices[5]),
    Segment(vertices[3], vertices[5]), Segment(vertices[3], vertices[4]), Segment(vertices[4], vertices[5]), Segment(vertices[4], vertices[6]),
    Segment(vertices[5], vertices[6]), Segment(vertices[5], vertices[8]), Segment(vertices[7], vertices[8]), Segment(vertices[6], vertices[8])
]

trapezoidal_map = TrapezoidalMap(edges)
trapezoidal_map.build()

# Приклад точки для локалізації
test_point = Point(10, 7)
located_trapezoid = trapezoidal_map.locate_point(test_point)

if located_trapezoid:
    print(f"Точка знаходиться в трапеції з координатами: ліво={located_trapezoid.left}, право={located_trapezoid.right}, низ={located_trapezoid.bottom}, верх={located_trapezoid.top}")
else:
    print("Точка не знаходиться в жодній з трапецій.")

plot_trapezoidal_map(trapezoidal_map, test_point)
