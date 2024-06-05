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

    def contains_point(self, point):
        if (point.x - self.p1.x) * (self.p2.y - self.p1.y) != (point.y - self.p1.y) * (self.p2.x - self.p1.x):
            return False
        if min(self.p1.x, self.p2.x) <= point.x <= max(self.p1.x, self.p2.x) and min(self.p1.y, self.p2.y) <= point.y <= max(self.p1.y, self.p2.y):
            return True
        return False

def read_vertices(filename):
    with open(filename, 'r') as f:
        vertices = []
        for line in f:
            x, y = map(float, line.strip().split())
            vertices.append(Point(x, y))
        return vertices

def read_edges(filename, vertices):
    with open(filename, 'r') as f:
        edges = []
        for line in f:
            start, end = map(int, line.strip().split())
            edges.append(Segment(vertices[start], vertices[end]))
        return edges

def localize_point(point, edges):
    for i, edge in enumerate(edges):
        if edge.contains_point(point):
            return i
    return None

def plot_graph(vertices, edges, point, highlight_edge_index=None):
    fig, ax = plt.subplots()
    # Plot edges and vertices
    for i, edge in enumerate(edges):
        plt.plot([edge.p1.x, edge.p2.x], [edge.p1.y, edge.p2.y], 'b-', linewidth=1)
        # Add text label near the middle of the segment
        mid_point = Point((edge.p1.x + edge.p2.x) / 2, (edge.p1.y + edge.p2.y) / 2)
        plt.text(mid_point.x, mid_point.y, f'{i}', color='purple', fontsize=12)
    for vertex in vertices:
        plt.plot(vertex.x, vertex.y, 'ro')
    # Highlight the edge if point is on it
    if highlight_edge_index is not None:
        edge = edges[highlight_edge_index]
        plt.plot([edge.p1.x, edge.p2.x], [edge.p1.y, edge.p2.y], 'g-', linewidth=2)
    # Plot the test point
    plt.plot(point.x, point.y, 'yo', markersize=10)
    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.title('Візуалізація графу з виділеною точкою')
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Зчитування даних з файлів
vertices = read_vertices('vertices.txt')
edges = read_edges('edges.txt', vertices)

# Приклад точки для локалізації
test_point = Point(11, 7)  # Змініть координати для різних тестів
found_edge_index = localize_point(test_point, edges)

if found_edge_index is not None:
    print(f"Точка знаходиться на ребрі з індексом {found_edge_index}.")
    plot_graph(vertices, edges, test_point, found_edge_index)
else:
    print("Точка не знаходиться на жодному з ребер.")
    plot_graph(vertices, edges, test_point)
