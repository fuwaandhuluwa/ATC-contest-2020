import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f_cost = sys.maxsize
        self.g_cost = sys.maxsize
        self.next = None
        self.matched = False
        self.visited = False


max_row = 0
max_col = 0


def generateRoadMap(points):
    global max_row
    global max_col
    for content in points:
        if not content:
            continue
        if len(content) == 1:
            continue
        x = int(content[0])
        y = int(content[1])
        if x > max_row:
            max_row = x
        if y > max_col:
            max_col = y

    max_row += 2
    max_col += 2
    road_map = [[None for i in range(0,max_col)] for j in range(0,max_row)]
    for content in points:
        if not content:
            continue
        if len(content) == 1:
            continue
        x = int(content[0])
        y = int(content[1])
        road_map[x][y] = Point(x, y)
    return road_map


class AStar:
    def __init__(self, road_map):
        self.roadMap = road_map
        self.open_set = set()
        self.close_set = set()
        self.max_row = max_row
        self.max_col = max_col
        self.adjacent = [[1, 0], [0, 1], [0, -1], [-1, 0]]  # right, up, down, left

    # Distance to start point
    def gCost(self, current: Point, parent: Point):
        return parent.g_cost + 1

    def hCost(self, current: Point, target: Point):
        dx = current.x - target.x
        dy = current.y - target.y
        if dx < 0:
            dx = - dx
        if dy < 0:
            dy = - dy
        return dx + dy

    def fCost(self, current: Point, target: Point):
        return current.g_cost + self.hCost(current, target)

    def isVisited(self, current: Point):
        return current.visited

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
        min_cost_point = None
        for i in self.open_set:
            if i.f_cost < min_cost:
                min_cost = i.f_cost
                min_cost_point = i
        return min_cost_point

    def resetVisitFlag(self):
        for i in self.open_set:
            i.visited = False
        for j in self.close_set:
            j.visited = False

    def search(self, start: Point, target: Point):
        start.f_cost = 0
        start.g_cost = 0
        self.resetVisitFlag()
        self.open_set.clear()
        self.close_set.clear()
        start.visited = True
        self.open_set.add(start)

        while len(self.open_set) > 0:
            current = self.selectMinCostPointInOpenList()
            next = self.roadMap[current.x][current.y].next
            if not self.isStartPoint(current, start):
                if next is None and current.matched is False or self.isTargetPoint(current, target):
                    return self.buildPath(current, start)
                else:
                    next.parent = current
                    next.g_cost = current.g_cost + 1
                    next.f_cost = next.g_cost + self.hCost(next, target)
                    next.visited = True
                    self.close_set.add(next)
            else:
                next = current

            self.open_set.remove(current)
            self.close_set.add(current)

            # process all neighbors
            for adjacent in self.adjacent:
                if self.roadMap[next.x + adjacent[0]][next.y + adjacent[1]] is not None:
                    self.ProcessPoint(self.roadMap[next.x + adjacent[0]][next.y + adjacent[1]], next, start, target)

    def ProcessPoint(self, current, parent, start, target):
        if current.visited:
            return

        current.parent = parent
        current.g_cost = parent.g_cost + 1
        current.f_cost = current.g_cost + self.hCost(current, target)
        current.visited = True
        self.open_set.add(current)

    def buildPath(self, point: Point, start: Point):
        index = 0
        point1 = None
        while True:
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


def run(points):
    special_road_map = generateRoadMap(points)
    a_star = AStar(special_road_map)
    points_size = len(points)
    for i in range(points_size):
        if special_road_map[points[i][0]][points[i][1]].matched is True:
            continue
        for j in range(i + 1, points_size):
            if special_road_map[points[j][0]][points[j][1]].matched is True:
                continue
            a_star.search(special_road_map[points[i][0]][points[i][1]], special_road_map[points[j][0]][points[j][1]])
            break
    stations_list = []
    for i in range(max_row):
        for j in range(max_col):
            station = []
            if special_road_map[i][j] is None:
                continue
            if special_road_map[i][j].matched is False:
                station.append((i, j))
                special_road_map[i][j] = None
            else:
                next = special_road_map[i][j].next
                station.append((i, j))
                station.append((next.x, next.y))
                special_road_map[next.x][next.y] = None
                special_road_map[i][j] = None
            stations_list.append(station)
    print(stations_list)
    return stations_list


def solution(count: int, points: list) -> list:
    return run(points)
    """
    :param count: total points count, e.g. 5
    :param points: point list, e.g. [(1,2),(1,3),(2,3),(3,3),(4,3)]
    :return list of points, e.g. [[(1,2),(1,3)],[(2,3),(3,3)],[(4,3)]]
    Take 2 white spaces as tab
    """


#solution(1, readFileContent("C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/17.in"))
points_raw = [(1, 1), (2, 1), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3), (2, 4)]
solution(1, points_raw)