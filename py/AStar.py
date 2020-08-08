# AStar Algorithm
# Reference document https://zhuanlan.zhihu.com/p/54510444

import numpy as np
from py.Point import Point
import time
import sys
from matplotlib.patches import Rectangle


class AStar:
    def __init__(self, road_map, d=1):
        self.map = road_map
        self.open_set = []   # store ready to search points
        self.close_set = []  # store searched points
        self.D = d  # Cost between two adjacent nodes

    # Distance to target point
    def hCost(self, current, target):
        dx = abs(current.x - target.x)
        dy = abs(current.y - target.y)
        return self.D * (dx + dy)

    # Distance to start point
    def gCost(self, current, start):
        dx = abs(current.x - start.x)
        dy = abs(current.y - start.y)
        return self.D * (dx + dy) + (np.sqrt(2) - 2 * self.D) * min(dx, dy)

    def fCost(self, current, start, target):
        return self.gCost(current, start) + self.hCost(current, target)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.isObstacle(x, y)

    def IsInPointList(self, point, point_list):
        for pointItem in point_list:
            if point.x == pointItem.x and point.y == pointItem.y:
                return True
        return False

    def IsInOpenList(self, point):
        return self.IsInPointList(point, self.open_set)

    def IsInCloseList(self, point):
        return self.IsInPointList(point, self.close_set)

    def IsTargetPoint(self, current, target):
        if current.x == target.x and current.y == target.y:
            return True
        return False

    def IsStartPoint(self, current, start):
        return self.IsTargetPoint(current, start)

    def search(self, ax, plt, start: Point, target: Point):
        start_time = time.time()

        start.cost = 0
        self.open_set.append(start)
        while True:
            # find the min cost point
            index = self.selectPointInOpenList()
            if index < 0:
                print("No path found, algorithm failed!!!")
                return

            current = self.open_set[index]
            rec = Rectangle((current.x, current.y), 1, 1, color='c')
            ax.add_patch(rec)
            self.SaveImage(plt)

            if self.IsTargetPoint(current, target):
                return self.buildPath(current, start, ax, plt, start_time)

            self.open_set.remove(current)
            self.close_set.append(current)

            # Process all neighbors
            upPoint = Point(current.x, current.y + 1)
            downPoint = Point(current.x, current.y - 1)
            rightPoint = Point(current.x + 1, current.y)
            leftPoint = Point(current.x - 1, current.y)
            self.ProcessPoint(leftPoint, current, start, target)
            self.ProcessPoint(downPoint, current, start, target)
            self.ProcessPoint(rightPoint, current, start, target)
            self.ProcessPoint(upPoint, current, start, target)

    def ProcessPoint(self, current, parent, start, target):
        if not self.IsValidPoint(current.x, current.y):
            return  # Do nothing for invalid point
        if self.IsInCloseList(current):
            return  # Do nothing for visited point
        if not self.IsInOpenList(current):
            current.parent = parent
            current.cost = self.fCost(current, start, target)
            self.open_set.append(current)
            print('Process Point [', current.x, ',', current.y, ']', ', cost: ', current.cost)

    def selectPointInOpenList(self):
        index = 0
        select_index = -1
        minvalue = sys.maxsize
        for point in self.open_set:
            if point.cost < minvalue:
                minvalue = point.cost
                select_index = index
            index += 1
        return select_index

    def buildPath(self, point: Point, start: Point, ax, plt, start_time):
        path = []
        while True:
            path.insert(0, point)
            if self.IsStartPoint(point, start):
                break
            else:
                point = point.parent

        for point in path:
            rec = Rectangle((point.x, point.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()
            self.SaveImage(plt)
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time - start_time), ' seconds')

    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)







