import numpy as np


def plane_equation(p1, p2, p3):
    """
    returns the plane equation's coefficients with given points p1, p2, p3
    p1: (x1, y1, z1)
    p2: (x2, y2, z2)
    p3: (x3, y3, z3)

    return a, b, c, d where ax + by + cz = d
    """
    p1_p2 = [p2[i] - p1[i] for i in range(len(p1))]
    p1_p3 = [p3[i] - p1[i] for i in range(len(p1))]

    normal = np.cross(p1_p2, p1_p3)
    a, b, c = normal
    d = np.dot(normal, p1)
    return a, b, c, d

def is_point_outside(face, point, epsilon=1e-6):
    """
    check if the point is outside the face
    face:  list of 3 points: [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]
    point: (x, y, z) of a point

    check if ax + by + cz > d, return True if it is
    """
    a, b, c, d = plane_equation(face)
    x, y, z = point
    return a * x + b * y + c * z - d > epsilon

def perpendicular_dist(face, point: list):
    """
    returns the perpendicular distance from the point to the face
    face: list of 3 points: [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]
    point: (x, y, z) of a point not on the face

    return the distance from the point to the face
    """

    a, b, c, d = plane_equation(face)
    x, y, z = point
    return abs(a * x + b * y + c * z - d) / (a ** 2 + b ** 2 + c ** 2) ** 0.5

def find_farthest_point(face, points):

    """
    find the fathest point from a face in a set of points
    face: list of 3 points: [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]
    points: list of points [(x1, y1, z1), (x2, y2, z2), ...]

    return the farthest point from the face
    """
    # init the max distance and the farthest point
    max_dist = -1
    farthest_point = None
    
    # loop through all points to find the farthest point
    for point in points:
        distance = perpendicular_dist(face, point)
        if distance > max_dist:
            max_dist = distance
            farthest_point = point
    
    return farthest_point

def get_edges(face: list):
    """
    get the edges of a face
    face: list of 3 points: [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]

    return the edges of the face: [(p1, p2), (p2, p3), (p3, p1)]
    """
    p1, p2, p3 = face
    return [(p1, p2), (p2, p3), (p3, p1)]
