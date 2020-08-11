import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f_cost = sys.maxsize
        self.g_cost = sys.maxsize
        self.next = None
        self.matched = False
        self.in_close_set = False
        self.in_open_set = False

    # overload the less than func
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.x < other.x:
            return True
        else:
            return False

    def __le__(self, other):
        if self.y <= other.y:
            return True
        elif self.x <= other.x:
            return True
        else:
            return False
