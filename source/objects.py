#!/usr/bin/python
import uuid
import math

def new_handle(arg_handle = False):
    if not arg_handle:
        return arg_handle
    else:
        return uuid.uuid4()

def distance_between_points(p1, p2):
    x_dist = p2.x - p1.x
    y_dist = p2.y - p1.y
    elev_dist = p2.elev - p1.elev
    return math.sqrt(x_dist ^ 2 + y_dist ^ 2 + elev_dist ^ 2)

class Point:
    def __init__(self, arg_x = 0.0, arg_y = 0.0, arg_elev = 0.0, arg_handle = False):
        self.x = arg_x
        self.y = arg_y
        self.elev = arg_elev
        self.handle = new_handle(arg_handle)

class Line:
    def __init__(self, arg_p1 = Point(), arg_p2 = Point(), arg_center_point = False, arg_handle = False):
        self.point1 = arg_p1
        self.point2 = arg_p2
        if not arg_center_point and type(arg_center_point) is Point and _is_valid_center_point(arg_center_point):
            self.center_point = arg_center_point
        else:
            self.center_point = None
        self.handle = new_handle(arg_handle)

    def _is_valid_center_point(arg_center_point):
        return true if distance_between_points(arg_center_point, point1) == distance_between_points(arg_center_point, point2) else false

class Polyline:
    def __init__(self, arg_handle = False, *arg):
        self.elements = {}
        self.handle = new_handle(arg_handle)
        #if len(arg > 0):
        #    for argument in arg:
        #        self.elements[arg.handle] = (