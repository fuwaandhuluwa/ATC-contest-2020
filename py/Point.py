import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f_cost = sys.maxsize
        self.g_cost = sys.maxsize
        self.next = None
        self.matched = False
