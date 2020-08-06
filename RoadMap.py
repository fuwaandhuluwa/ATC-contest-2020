import numpy as np
from Point import Point


class RandomMap:
    def __init__(self, size=50):  # size is the road map size
        self.obstacle_point = []
        self.size = size
        self.obstacle = size // 8
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point.append(Point(self.size // 2, self.size // 2))
        self.obstacle_point.append(Point(self.size // 2, self.size // 2 - 1))

        # Generate an obstacle in the middle
        for i in range(self.size//2-4, self.size//2):
            self.obstacle_point.append(Point(i, self.size - i))
            self.obstacle_point.append(Point(i, self.size - i - 1))
            self.obstacle_point.append(Point(self.size - i, i))
            self.obstacle_point.append(Point(self.size - i - 1, i))

        # Random generate some obstacle
        for i in range(self.obstacle - 1):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(Point(x, y))

            if np.random.rand() > 0.5:  # Random boolean
                for j in range(self.size // 4):
                    self.obstacle_point.append(Point(x, y + j))
                    pass
            else:
                for j in range(self.size // 4):
                    self.obstacle_point.append(Point(x + j, y))
                    pass

    def isObstacle(self, x, y):
        for point in self.obstacle_point:
            if point.x == x and point.y == y:
                return True
        return False





