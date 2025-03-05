This is my learning process in convex hull algorithm.

Currently only the 2D version is finished. I will soon working on the 3D version.

Some preknowledge of 2D version of the convex hull algorithm:
1. Vector cross product (this helps understand whether a point is located on the upper/left or lower/right side of a line)
2. Recursive algorithm (this helps recursively find new point that is beyond current process)

Also a quick tip in finding `min` points by components in the list: 

```python
# suppose there is a list of points, each point in (x, y) format:
number = [(3, 2), (8, 1), (10, 6)]
smallest_x_number = min(number, key=lambda p: p[0]);
smallest_y_number = min(number, key=lambda p: p[1]);

print("The smallest x number is:", smallest_x_number)  # expected output: (3, 2)
print("The smallest y number is:", smallest_y_number)  # expected output: (8, 1)
```
Some key geometry problems in this 2D convex hull:
1. The concept on how to judge if point $C$ is on the upper/left side of line $AB$ or on the right side of line $AB$:
![Judge if $C$ is on upper or lower side of line $AB$](images/judge_C_on_which_side_AB.png)
2. How to find the distance from a point to a line. Here is 2 approaches I have derived to describe this problem (I recommend approach 2 if you are familiar with vector knowledge): 
![Compute distance from point to a line - Approach 1](images/find_distance_point_line_1.png)
![Compute distance from point to a line - Approach 2](images/find_distance_point_line_2.png)
