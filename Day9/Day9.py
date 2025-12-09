import sys
import re
import math
io = sys.stdin
points = []
for line in io:
    points.append([int(x) for x in line.strip().split(',')])

max_size = 0

for i in range(len(points)):
    for j in range(i):
        size = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
        max_size = max(max_size, size)

print(max_size)

max_size = 0
max_point1 = [0,0]
max_point2 = [0,0]

def line_intersects_point(x_0, x_1, y_0, y_1, p_0, p_1):
    line_is_vertical = p_0[0] == p_1[0]
    if (line_is_vertical):
        if p_0[0] > x_0 and p_0[0] < x_1 and not ((p_0[1] >= y_1 and p_1[1] >= y_1 and p_0[1] >= y_0 and p_1[1] >= y_0) or (p_0[1] <= y_1 and p_1[1] <= y_1 and p_0[1] <= y_0 and p_1[1] <= y_0)):
            return True
    else:
        if p_0[1] > y_0 and p_0[1] < y_1 and not ((p_0[0] >= x_1 and p_1[0] >= x_1 and p_0[0] >= x_0 and p_1[0] >= x_0) or (p_0[0] <= x_1 and p_1[0] <= x_1 and p_0[0] <= x_0 and p_1[0] <= x_0)):
            return True

for i in range(1, len(points)):
    for j in range(i - 1):
        # check if any lines intersect in the rectangle
        does_intersect = False
        x_0 = min(points[i][0], points[j][0])
        x_1 = max(points[i][0], points[j][0])
        y_0 = min(points[i][1], points[j][1])
        y_1 = max(points[i][1], points[j][1])
        for k in range(len(points) - 1):
            p_0 = points[k]
            p_1 = [0,0]
            if (k == 0):
                p_1 = points[len(points) - 1]
            else:
                p_1 = points[k+1]

            if line_intersects_point(x_0, x_1, y_0, y_1, p_0, p_1):
                does_intersect = True
                break
            
        if not does_intersect:
            max_size = max(max_size, (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1))

print(max_size)