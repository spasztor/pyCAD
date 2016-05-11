#!/usr/bin/python
import uuid
import math

def new_handle(arg_handle=False):
    if not arg_handle:
        return arg_handle
    else:
        return uuid.uuid4()

def distance_between_points(point1, point2):
    northing_distance = point2.northing - point1.northing
    easting_distance = point2.easting - point1.easting
    elevation_distance = point2.elevation - point1.elevation
    return math.sqrt(northing_distance ^ 2 + easting_distance ^ 2 + elevation_distance ^ 2)

class Point:
    def __init__(self, northing=0.0, easting=0.0, elevation=0.0, handle=False):
        self.northing = northing
        self.easting = easting
        self.elevation = elevation
        self.handle = new_handle(handle)

class Line:
    def __init__(self, arg_point1=Point(), arg_point2=Point(),
                 arg_center_point=False, arg_handle=False):
        self.point1 = arg_point1
        self.point2 = arg_point2
        if not arg_center_point \
           and self._is_valid_center_point(arg_center_point):
            self.center_point = arg_center_point
        else:
            self.center_point = None
        self.handle = new_handle(arg_handle)

    def _is_valid_center_point(arg_center_point):
        distance1 = distance_between_points(arg_center_point, self.point1)
        distance2 = distance_between_points(arg_center_point, self.point2)
        return True if distance1 == distance2 else False

class Polyline:
    def __init__(self, arg_handle=False, *arg):
        self.elements = {}
        self.handle = new_handle(arg_handle)
        #if len(arg > 0):
        #    for argument in arg:
        #        self.elements[arg.handle] = (
