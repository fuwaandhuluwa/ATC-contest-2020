# main.py

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import py.RoadMap
from py.AStar import AStar
from py.Point import Point

plt.figure(figsize=(5, 5))

map = py.RoadMap.RandomMap()

ax = plt.gca()
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])

for i in range(map.size):
    for j in range(map.size):
        if map.isObstacle(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

rec = Rectangle((0, 0), width=1, height=1, facecolor='b')
ax.add_patch(rec)

rec = Rectangle((map.size-1, map.size-1), width=1, height=1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()

a_start = AStar(map)
a_start.search(ax, plt, Point(0, 0), Point(map.size-1, map.size-1))

plt.show()