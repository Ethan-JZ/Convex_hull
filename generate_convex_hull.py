import matplotlib.pyplot as plt
from helper import plane_equation, is_point_outside, find_farthest_point, get_edges
from matplotlib.patches import Polygon

class ConvexHullQuickHull:

    def __init__(self, points: list, dimension: int):
        self.points    = points
        self.dimension = dimension
    
    def quickhull_2D(self):

        if len(self.points) <= 3:
            return self.points  # base case, all points are part of the hull
        
        # Find leftmost and rightmost points
        point_A = min(self.points, key=lambda p: p[0])
        point_B = max(self.points, key=lambda p: p[0])

        # Divide points into upper and lower of AB
        left_points  = [p for p in self.points if self.is_left_2D(point_A, point_B, p)]
        right_points = [p for p in self.points if self.is_left_2D(point_B, point_A, p)]

        # Find the hull for upper and lower subsets
        upper_hull = self.find_hull_2D(point_A, point_B, left_points)
        lower_hull = self.find_hull_2D(point_B, point_A, right_points)

        # combine the results
        return [point_A] + upper_hull + [point_B] + lower_hull  # the order matters, as the correct order forms the closed loop of the hull
    
    def quickhull_3D(self):
        
        # base case
        if len(self.points) < 4:
            return self.points
        
        # Init the convex hull as a tetrahedron
        hull_points = self.create_tetrahedron(self.points)
        hull_faces  = []

        # create the init faces for the tetrahedron
        p1, p2, p3, p4 = hull_points
        hull_faces.append([p1, p2, p3])
        hull_faces.append([p1, p3, p4])
        hull_faces.append([p1, p2, p4])
        hull_faces.append([p2, p3, p4])

        # find the points outside each face of the tetrahedron
        for face in hull_faces:
            outside_points = [point for point in self.points if is_point_outside(face, point)]

            if outside_points:
                farthest_point = find_farthest_point(face, outside_points)
                hull_faces = self.update_hull(hull_faces, face, farthest_point)
        
        return hull_faces
    
    def update_hull(self, hull_faces: list, face, farthest_point):
        """
        update the hull with the farthest point
        """

        # remove the current face
        hull_faces.remove(face)

        # add new faces formed by the farthest point and edges of the current face
        new_faces = []

        for edge in get_edges(face):
            new_face = plane_equation([edge[0], edge[1], farthest_point])
            new_faces.append(new_face)
        
        hull_faces.extend(new_faces)

        return hull_faces

    @staticmethod
    def find_extreme_points_3D(points: list) -> list:

        """
        find the extreme points in 3D space on each axis: x y z direction
        """
        min_x, max_x = min(points, key=lambda p: p[0]), max(points, key=lambda p: p[0])
        min_y, max_y = min(points, key=lambda p: p[1]), max(points, key=lambda p: p[1])
        min_z, max_z = min(points, key=lambda p: p[2]), max(points, key=lambda p: p[2])

        return [min_x, max_x, min_y, max_y, min_z, max_z]
    
    def create_tetrahedron(self, points: list) -> list:

        extreme_points = self.find_extreme_points_3D(points)

        # create the tetrahedron from 4 non-coplanar points
        tetrahedron = [extreme_points[i] for i in range(0, 6, 2)]
        return tetrahedron

    def find_hull_2D(self, point_A, point_B, points):

        if not points:
            return []
        
        # Find the farthest point from AB
        point_C = max(points, key=lambda p: self.find_distance_point_line(point_A, point_B, p))

        # divide points to those outside triangle ABC
        left_AC_points  = [p for p in points if self.is_left_2D(point_A, point_C, p)]
        left_CB_points  = [p for p in points if self.is_left_2D(point_C, point_B, p)]

        # recursively find the hull for new subsets
        hull_beyond_AC = self.find_hull_2D(point_A, point_C, left_AC_points)
        hull_beyond_CB = self.find_hull_2D(point_C, point_B, left_CB_points)

        return hull_beyond_AC + [point_C] + hull_beyond_CB
    
    @staticmethod
    def is_left_2D(point_A, point_B, p):
        flag = (point_B[0] - point_A[0]) * (p[1] - point_B[1]) - (p[0] - point_B[0]) * (point_B[1] - point_A[1]) > 0
        return flag
    
    @staticmethod
    def find_distance_point_line(point_A, point_B, point):
        
        # find k and b of the line formed by point A and point B
        slope_k = (point_B[1] - point_A[1]) / (point_B[0] - point_A[0])
        bias_b  = point_A[1] - slope_k * point_A[0]
        
        # find the distance from point to line AB
        x, y = point[0], point[1]
        distance = abs(slope_k * x - y + bias_b) / (slope_k ** 2 + 1) ** 0.5
        
        return distance

    def plot_convex_hull(self):

        if self.dimension == 2:  # plot the points if it's 2D
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

            # plotting for ax1: just the points
            x = [point[0] for point in self.points]
            y = [point[1] for point in self.points]
            ax1.scatter(x, y, s=30, edgecolors="black", marker="o", c='orange')
            ax1.set_xlabel("X")
            ax1.set_ylabel("Y")
            ax1.grid()
         
            # plotting for ax2: points and the convex hull
            # get the convex hull points set
            convexhull = self.quickhull_2D()
            x_convex   = [point[0] for point in convexhull]
            y_convex   = [point[1] for point in convexhull]

            # append the first point to close the convex
            x_convex.append(x_convex[0])
            y_convex.append(y_convex[0])

            # Create the polygon
            polygon = Polygon(convexhull, closed=True, facecolor='lightblue', edgecolor='black')
            ax2.add_patch(polygon)
            
            # draw the convex hull
            plt.plot(x_convex, y_convex, c="black", mec="black", marker="o", ms=10, mfc="red")
            
            # draw the points set
            ax2.scatter(x, y, s=30, edgecolors="black", marker="o", c='orange')
            ax2.set_xlabel("X")
            ax2.set_ylabel("Y")
            
            ax2.grid()
            plt.show()
        