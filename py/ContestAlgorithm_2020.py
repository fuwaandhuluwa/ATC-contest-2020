# encoding=utf-8

from py.Point import Point
import numpy as np
from py.readFileList import getFileList, readFileContent
import sys
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import time
import heapq

max_row = 0
max_col = 0
Points = []


def getFile():
    file_list = getFileList(extension='.in')
    file_id = 0
    for file in file_list:
        print(file_id, file)
        file_id += 1
    file_id = int(input("please input file number:"))
    global max_row
    global max_col
    max_row = 0
    max_col = 0
    points = readFileContent(file_list[file_id])
    return points


def generateRoadMap(points):
    global max_row
    global max_col
    # print(points)
    for content in points[1:]:
        if not content:
            continue
        content = content.split(',')
        x = int(content[0])
        y = int(content[1])
        if x > max_row:
            max_row = x
        if y > max_col:
            max_col = y

    max_row += 1
    max_col += 1
    road_map = np.ndarray([max_row, max_col], dtype=Point)
    for content in points[1:]:
        if not content:
            continue
        content = content.split(',')
        x = int(content[0])
        y = int(content[1])
        road_map[x][y] = Point(x, y)
        Points.append(road_map[x][y])

    #    print(road_map)
    return road_map


class AStar:
    def __init__(self, road_map):
        self.roadMap = road_map
        self.open_set = []
        self.close_set = []
        self.max_row = max_row
        self.max_col = max_col
        self.adjacent = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        # self.initRoadMap()

    def initRoadMap(self):
        for i in range(max_row):
            for j in range(max_col):
                if self.roadMap[i][j] is None or self.roadMap[i][j].matched is True:
                    continue

                for point in self.adjacent:
                    if self.isValidPoint(i + point[0], j + point[1]) is True \
                            and self.roadMap[i + point[0]][j + point[1]] is not None \
                            and self.roadMap[i + point[0]][j + point[1]].matched is False:
                        self.roadMap[i][j].next = self.roadMap[i + point[0]][j + point[1]]
                        self.roadMap[i + point[0]][j + point[1]].next = self.roadMap[i][j]
                        self.roadMap[i][j].matched = True
                        self.roadMap[i + point[0]][j + point[1]].matched = True
                        break

    # Distance to start point
    def gCost(self, current: Point, parent: Point):
        return parent.g_cost + 1

    def hCost(self, current: Point, target: Point):
        dx = abs(current.x - target.x)
        dy = abs(current.y - target.y)
        return dx + dy

    def fCost(self, current: Point, target: Point):
        return current.g_cost + self.hCost(current, target)

    def isInOpenList(self, current: Point):
        # for i in self.open_set:
        #     if i.x == current.x and i.y == current.y:
        #         return True
        # return False

        if current in self.open_set:
            return True
        return False

    def isInCloseList(self, current: Point):
        # for i in self.close_set:
        #     if i.x == current.x and i.y == current.y:
        #         return True
        # return False
        if current in self.close_set:
            return True
        return False

    def isTargetPoint(self, current: Point, target: Point):
        if current.x == target.x and current.y == target.y:
            return True
        return False

    def isStartPoint(self, current: Point, start: Point):
        if current.x == start.x and current.y == start.y:
            return True
        return False

    def selectMinCostPointInOpenList(self):
        min_cost = sys.maxsize
        index = 0
        select_index = -1
        for i in self.open_set:
            if i.f_cost < min_cost:
                min_cost = i.f_cost
                select_index = index
            index += 1
        return select_index

    def isValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.max_row or y >= self.max_col:
            return False
        return True

    def search(self, ax, plt, start: Point, target: Point):
        start.f_cost = 0
        start.g_cost = 0
        self.open_set.clear()
        self.close_set.clear()
        self.open_set.append(start)

        # rec = Rectangle((start.x, start.y), width=1, height=1, facecolor='b')
        # ax.add_patch(rec)
        #
        # rec = Rectangle((target.x, target.y), width=1, height=1, facecolor='r')
        # ax.add_patch(rec)

        while len(self.open_set) > 0:
            # index = self.selectMinCostPointInOpenList()
            # if index < 0:
            #     print('open set is empty! search done.')
            #     break
            #
            # current = self.open_set[index]
            current = heapq.nsmallest(1, self.open_set, key=lambda point: point.f_cost)[0]
            # rec = Rectangle((current.x, current.y), 1, 1, color='c')
            # ax.add_patch(rec)
            # self.SaveImage(plt)

            next = self.roadMap[current.x][current.y].next
            if not self.isStartPoint(current, start):
                if next is None and current.matched is False or self.isTargetPoint(current, target):
                    return self.buildPath(current, start, ax, plt)
                else:
                    # rec = Rectangle((next.x, next.y), 1, 1, color='c')
                    # ax.add_patch(rec)
                    # self.SaveImage(plt)
                    next.parent = current
                    next.g_cost = current.g_cost + 1
                    next.f_cost = self.fCost(next, target)
                    self.close_set.append(next)
            else:
                next = current

            self.open_set.remove(current)
            self.close_set.append(current)

            # process all neighbors
            for adjacent in self.adjacent:
                if self.isValidPoint(next.x + adjacent[0], next.y + adjacent[1]) \
                        and self.roadMap[next.x + adjacent[0]][next.y + adjacent[1]] is not None:
                    self.ProcessPoint(self.roadMap[next.x + adjacent[0]][next.y + adjacent[1]], next, start, target)

    def ProcessPoint(self, current, parent, start, target):
        # if not self.isValidPoint(current.x, current.y):
        #     return  # Do nothing for invalid point
        if self.isInCloseList(current):
            return  # Do nothing for visited point
        if not self.isInOpenList(current):
            current.parent = parent
            current.g_cost = self.gCost(current, start)
            current.f_cost = self.fCost(current, target)
            self.open_set.append(current)
            # print('Process Point [', current.x, ',', current.y, ']', ', cost: ', current.cost)

    def buildPath(self, point: Point, start: Point, ax, plt):
        path = []
        index = 0
        point1 = None
        while True:
            path.insert(0, point)
            if index == 0:
                point1 = point
                index += 1
            else:
                point.next = point1
                point.matched = True
                point1.next = point
                point1.matched = True
                index = 0

            if self.isStartPoint(point, start):
                break
            else:
                point = point.parent

        # for point in path:
        #     rec = Rectangle((point.x, point.y), 1, 1, color='g')
        #     ax.add_patch(rec)
        #     plt.draw()
            # self.SaveImage(plt)

    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)


# # main test program
# special_road_map = generateRoadMap(getFile())
# ax = plt.gca()
# ax.set_xlim([0, max_row])
# ax.set_ylim([0, max_col])
#
# for i in range(max_row):
#     for j in range(max_col):
#         if special_road_map[i][j] is None:
#             rec = Rectangle((i, j), width=1, height=1, color='gray')
#             ax.add_patch(rec)
#         else:
#             rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
#             ax.add_patch(rec)
#
# plt.axis('equal')
# plt.axis('off')
# plt.tight_layout()
# a_star = AStar(special_road_map)
# for i in range(len(Points)):
#     if special_road_map[Points[i].x][Points[i].y].matched is True:
#         continue
#     for j in range(i + 1, len(Points)):
#         if special_road_map[Points[j].x][Points[j].y].matched is True:
#             continue
#         a_star.search(ax, plt, Points[i], Points[j])
#         break
#
# station_number = 0
# for i in range(max_row):
#     for j in range(max_col):
#         if special_road_map[i][j] is None:
#             continue
#         if special_road_map[i][j].matched is False:
#             print("{}, {}".format(i, j))
#             special_road_map[i][j] = None
#         else:
#             next = special_road_map[i][j].next
#             print("{}, {}; {}, {}".format(i, j, next.x, next.y))
#             special_road_map[next.x][next.y] = None
#             special_road_map[i][j] = None
#         station_number += 1
# print("min station number: %d" % station_number)
# plt.show()

def run(points):
    # main test program
    Points.clear()
    special_road_map = generateRoadMap(points)
    ax = plt.gca()
    # ax.set_xlim([0, max_row])
    # ax.set_ylim([0, max_col])
    #
    # for i in range(max_row):
    #     for j in range(max_col):
    #         if special_road_map[i][j] is None:
    #             rec = Rectangle((i, j), width=1, height=1, color='gray')
    #             ax.add_patch(rec)
    #         else:
    #             rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
    #             ax.add_patch(rec)

    # plt.axis('equal')
    # plt.axis('off')
    # plt.tight_layout()
    a_star = AStar(special_road_map)
    for i in range(len(Points)):
        if special_road_map[Points[i].x][Points[i].y].matched is True:
            continue
        for j in range(i + 1, len(Points)):
            if special_road_map[Points[j].x][Points[j].y].matched is True:
                continue
            a_star.search(ax, plt, Points[i], Points[j])
            break

    station_number = 0
    for i in range(max_row):
        for j in range(max_col):
            if special_road_map[i][j] is None:
                continue
            if special_road_map[i][j].matched is False:
                # print("{}, {}".format(i, j))
                special_road_map[i][j] = None
            else:
                next = special_road_map[i][j].next
                # print("{}, {}; {}, {}".format(i, j, next.x, next.y))
                special_road_map[next.x][next.y] = None
                special_road_map[i][j] = None
            station_number += 1
    return station_number
