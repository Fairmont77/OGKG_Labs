#5. Перетин відрізків на площині (Bentley–Ottmann).
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations


def orientation(p, q, r):
    """Визначає орієнтацію трьох точок (за годинниковою стрілкою, проти годинникової стрілки або колінеарні)"""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def intersection_point(p1, q1, p2, q2):
    """ Знаходження точки перетину двох відрізків, якщо вони перетинаються """
    A1 = q1[1] - p1[1]
    B1 = p1[0] - q1[0]
    C1 = A1 * p1[0] + B1 * p1[1]
    A2 = q2[1] - p2[1]
    B2 = p2[0] - q2[0]
    C2 = A2 * p2[0] + B2 * p2[1]
    determinant = A1 * B2 - A2 * B1
    if determinant != 0:
        x = (B2 * C1 - B1 * C2) / determinant
        y = (A1 * C2 - A2 * C1) / determinant
        return (x, y)
    return None


def on_segment(p, q, r):
    """ Перевірка, чи точка r лежить на відрізку pq """
    if min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1]):
        return True
    return False


def check_intersect(p1, q1, p2, q2):
    """ Перевірка, чи перетинаються два відрізки """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if (o1 != o2 and o3 != o4):
        return True
    if (o1 == 0 and on_segment(p1, q1, p2)) or (o2 == 0 and on_segment(p1, q1, q2)) or (
            o3 == 0 and on_segment(p2, q2, p1)) or (o4 == 0 and on_segment(p2, q2, q1)):
        return True
    return False


def main():
    lines = [
        ((np.random.randint(0, 10), np.random.randint(0, 10)), (np.random.randint(0, 10), np.random.randint(0, 10))) for
        _ in range(20)]
    intersection_points = []

    for (p1, q1), (p2, q2) in combinations(lines, 2):
        if check_intersect(p1, q1, p2, q2):
            pt = intersection_point(p1, q1, p2, q2)
            if pt and on_segment(p1, q1, pt) and on_segment(p2, q2, pt):
                intersection_points.append(pt)

    plt.figure(figsize=(10, 10))
    for line in lines:
        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'b-')

    for pt in intersection_points:
        plt.scatter(*pt, color='yellow', s=80, zorder=5)

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
