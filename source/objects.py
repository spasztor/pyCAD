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
    """ Creates a new handle or returns the passed handle if it's valid. """
    try:
        if handle is not None and str(handle) == str(uuid.UUID(handle, version=4)):
            return handle
        else:
            return str(uuid.uuid4())
    except:
        return str(uuid.uuid4())


class Point:
    """ Point class containing a northing, easting, elevation and handle. """
    def __init__(self, northing=0.0, easting=0.0, elevation=0.0, handle=None):
        self.northing = northing
        self.easting = easting
        self.elevation = elevation
        self.handle = new_handle(handle)

    def __str__(self):
        return "{}, {}, {}".format(self.easting, self.northing, self.elevation)

class Line:
    """ Line class containing a starting point, end point, potential center_point and handle. """
    def __init__(self, start=Point(), end=Point(),
                 center_point=None, handle=None):
        self.start = start
        self.end = end
        self.center_point = center_point
        if self._is_valid_center_point():
            self.center_point = center_point
        self.handle = new_handle(handle)

    def _is_valid_center_point(self):
        """ Checks to see if the center_point is equadistant to the start and end point. """
        distance_to_start = Line(self.center_point, self.start).get_length()
        distance_to_end = Line(self.center_point, self.end).get_length()
        return True if distance_to_start == distance_to_end else False

    def get_length(self):
        """ Calculates the length of the line using northing, easting and elevation. """
        northing_distance = self.end.northing - self.start.northing
        easting_distance = self.end.easting - self.start.easting
        elevation_distance = self.end.elevation - self.start.elevation
        return math.sqrt(northing_distance ^ 2 + easting_distance ^ 2 + elevation_distance ^ 2)

class Polyline:
    """ A polyline object which is a dictionary of lines and a handle.
    """
    def __init__(self, handle=None, *arg):
        self.elements = {}
        self.handle = new_handle(handle)
        #if len(arg > 0):
        #    for argument in arg:
        #        self.elements[arg.handle] = (
