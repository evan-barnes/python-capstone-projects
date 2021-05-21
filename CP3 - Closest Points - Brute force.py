import numpy as np
from matplotlib import pyplot as plt
import math
import random

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_random_points(n):
    points = []
    while len(points) < n:
        x, y = random.randint(0,20), random.randint(0,20)
        if (x, y) not in points:
            points.append((x, y))
    return points

points = generate_random_points(20)

distances = []
for a in range(len(points) - 1):
    #print(test_points[a])
    for b in range(a + 1, len(points)):
        #print(f'\t{test_points[b]}')
        dist = distance(points[a],points[b])
        #print(f'\t\tDistance: {dist:.4f}')
        distances.append((points[a], points[b], dist))
        
ds = [d[2] for d in distances]
shortest = min(ds)
shortest_indices = []
for i, d in enumerate(ds): #use enumerate to find the index of multiple minima
    if d == shortest:
        shortest_indices.append(i)
shortest_lines = []
for index in shortest_indices:
    shortest_lines.append(distances[index][:2]) #removes distance to prepare these points for plotting
    #print(distances[index])
    
#plt.axis('equal')
plt.xticks(range(0,21,2))
plt.yticks(range(0,21,2))

for x, y in points:
    plt.plot(x,y,'bo')

for pair in shortest_lines:
    plotx, ploty = [i[0] for i in pair], [i[1] for i in pair]
    #print(plotx, ploty)
    plt.plot(plotx, ploty, 'r')
