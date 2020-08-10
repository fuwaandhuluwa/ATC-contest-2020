import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f_cost = sys.maxsize
        self.g_cost = sys.maxsize
        self.next = None
        self.matched = False

    # overload the less than func for priority queue
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.x < other.x:
            return True
        else:
            return False
