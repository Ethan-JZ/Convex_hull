from generate_random_points import PointsGenerator
from generate_convex_hull import ConvexHullQuickHull


# create random points
points_set_model = PointsGenerator(dimension=2, number_range=[0, 5], number_points=10)
points_set = points_set_model.points
points_set_model.plot_points()

# generate convex hull of such poins set
hull_model = ConvexHullQuickHull(points=points_set, dimension=2)
hull_model.plot_convex_hull()