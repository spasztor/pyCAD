#!/usr/bin/python
import uuid
import math

def new_handle(arg_handle=False):
    if not arg_handle:
        return arg_handle
    else:
        return uuid.uuid4()

class Point:
    def __init__(self, northing=0.0, easting=0.0, elevation=0.0, handle=False):
        self.northing = northing
        self.easting = easting
        self.elevation = elevation
        self.handle = new_handle(handle)

class Line:
    def __init__(self, start=Point(), end=Point(),
                 center_point=False, handle=False):
        self.start = start
        self.end = end
        if not center_point \
           and self._is_valid_center_point(center_point):
            self.center_point = center_point
        else:
            self.center_point = None
        self.handle = new_handle(handle)

    def _is_valid_center_point(center_point):
        distance_to_start = Line(center_point, self.start).get_length()
        distance_to_end = Line(center_point, self.end).get_length()
        return True if distance_to_start == distance_to_end else False

    def get_length(point1=self.start, point2=self.end)
        northing_distance = point2.northing - point1.northing
        easting_distance = point2.easting - point1.easting
        elevation_distance = point2.elevation - point1.elevation
        return math.sqrt(northing_distance ^ 2 + easting_distance ^ 2 + elevation_distance ^ 2)

class Polyline:
    def __init__(self, arg_handle=False, *arg):
        self.elements = {}
        self.handle = new_handle(arg_handle)
        #if len(arg > 0):
        #    for argument in arg:
        #        self.elements[arg.handle] = (
