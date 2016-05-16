#!/usr/bin/python
"""Object Module for pyCAD
This module defines the base along with their methods and a variety of helper functions.
Specifically this module contains the following:
    Functions:
        new_handle(handle) - Create a new handle from existing or new.
    Classes:
        Point(northing, easting, elevation, handle) - A basic point object.
        Line(start, end, center_point, handle) - A line object that can also be an arc if you wish.
        Polyline() - A dictionary of lines.
"""
import uuid
import math

def new_handle(handle=None):
    """ Creates a new handle from an existing one or a new one if None is specified."""
    if handle is not None:
        return handle
    else:
        return uuid.uuid4()

class Point:
    """ A basic point object with a northing, easting, elevation and handle.
        
    """
    def __init__(self, northing=0.0, easting=0.0, elevation=0.0, handle=None):
        self.northing = northing
        self.easting = easting
        self.elevation = elevation
        self.handle = new_handle(handle)

class Line:
    def __init__(self, start=Point(), end=Point(),
                 center_point=None, handle=None):
        self.start = start
        self.end = end
        if center_point is not None \
           and self._is_valid_center_point(center_point):
            self.center_point = center_point
        else:
            self.center_point = None
        self.handle = new_handle(handle)

    def _is_valid_center_point(self, center_point):
        distance_to_start = Line(center_point, self.start).get_length()
        distance_to_end = Line(center_point, self.end).get_length()
        return True if distance_to_start == distance_to_end else False

    def get_length(self, point1=None, point2=None):
        point1 = self.start
        point2 = self.end
        northing_distance = point2.northing - point1.northing
        easting_distance = point2.easting - point1.easting
        elevation_distance = point2.elevation - point1.elevation
        return math.sqrt(northing_distance ^ 2 + easting_distance ^ 2 + elevation_distance ^ 2)

class Polyline:
    def __init__(self, handle=None, *arg):
        self.elements = {}
        self.handle = new_handle(handle)
        #if len(arg > 0):
        #    for argument in arg:
        #        self.elements[arg.handle] = (
