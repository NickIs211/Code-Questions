import math


def closestk(points, k):
    def dist(tupl): return math.hypot(*tupl)
    return sorted(points, key=dist)[:k]


points = [(1, 2), (8, 1), (4, 5), (8, 2)]
print(closestk(points, 2))
