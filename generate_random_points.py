import random
import matplotlib.pyplot as plt


class PointsGenerator:

    def __init__(self, dimension: int, number_range: list, number_points: int) -> None:
        self.dimension     = dimension
        self.number_range  = number_range
        self.number_points = number_points
        self.points = self.generate_random_number()
    
    def generate_random_number(self):

        # generate random number from given range
        points = []
        
        if self.dimension == 2:
            for _ in range(self.number_points):
                x = random.uniform(self.number_range[0], self.number_range[1])
                y = random.uniform(self.number_range[0], self.number_range[1])
                points.append((x, y))
        
        elif self.dimension  == 3:
            for _ in range(self.number_points):
                x = random.uniform(self.number_range[0], self.number_range[1])
                y = random.uniform(self.number_range[0], self.number_range[1])
                z = random.uniform(self.number_range[0], self.number_range[1])

                points.append((x, y, z))
        
        return points
    
    def plot_points(self):
        
        if self.dimension == 2:  # plot the points if it's 2D
            fig, ax = plt.subplots(figsize=(5, 5))
            x = [point[0] for point in self.points]
            y = [point[1] for point in self.points]
            ax.scatter(x, y, s=20, edgecolors="black", marker="o", c='orange')
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            plt.grid()
            plt.show()
            
        elif self.dimension == 3:  # plot the points if it's 3D
            fig = plt.figure()
            ax  = fig.add_subplot(projection='3d')
            x = [point[0] for point in self.points]
            y = [point[1] for point in self.points]
            z = [point[2] for point in self.points]
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")

            ax.scatter(x, y, z, s=20, edgecolors="black", marker="o", c='orange')
            plt.grid()
            plt.show()