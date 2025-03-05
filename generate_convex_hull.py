import matplotlib.pyplot as plt


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
        upper_points = [p for p in self.points if self.is_upper_2D(point_A, point_B, p)]
        lower_points = [p for p in self.points if self.is_upper_2D(point_B, point_A, p)]

        # Recursively find the hull for upper and lower subsets
        upper_hull = self.find_hull_2D(point_A, point_B, upper_points)
        lower_hull = self.find_hull_2D(point_B, point_A, lower_points)

        # combine the results
        return [point_A] + upper_hull + [point_B] + lower_hull  # the order matters, as the correct order forms the closed loop of the hull
    
    def find_hull_2D(self, point_A, point_B, points):

        if not points:
            return []
        
        # Find the farthest point from AB
        point_C = max(points, key=lambda p: self.find_distance_point_line(point_A, point_B, p))

        # divide points to those outside triangle ABC
        upper_points = [p for p in points if self.is_upper_2D(point_A, point_C, p)]
        lower_points = [p for p in points if self.is_upper_2D(point_C, point_B, p)]

        # recursively find the hull for new subsets
        above_AC = self.find_hull_2D(point_A, point_C, upper_points)
        above_CB = self.find_hull_2D(point_C, point_B, lower_points)

        return above_AC + [point_C] + above_CB
    
    @staticmethod
    def is_upper_2D(point_A, point_B, p):
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
            fig, ax = plt.subplots(figsize=(5, 5))
            x = [point[0] for point in self.points]
            y = [point[1] for point in self.points]

            # get the convex hull points set
            convexhull = self.quickhull_2D()
            x_convex   = [point[0] for point in convexhull]
            y_convex   = [point[1] for point in convexhull]

            # append the first point to close the convex
            x_convex.append(x_convex[0])
            y_convex.append(y_convex[0])
            
            # draw the convex hull
            plt.plot(x_convex, y_convex, c="black", mec="black", marker="o", ms=10, mfc="red")
            
            # draw the points set
            ax.scatter(x, y, s=30, edgecolors="black", marker="o", c='orange')
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            plt.grid()
            plt.show()
        