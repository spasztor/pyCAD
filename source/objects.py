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
NAME
SHORT_DESC
LONG_DESC
COPYRIGHT
LICENSE
"""
import uuid
import math
import exceptions #from pyCAD import exceptions

def new_handle(handle=None):
    """ SHORT_DESC
        LONG_DESC
        ARG
        RETURNS
        RAISES
    Creates a new handle or returns the passed handle if it's valid.
    """
    return handle if handle is not None and str(handle) == \
        str(uuid.UUID(handle, version=4)) else str(uuid.uuid4())

class Point:
    """ Point class containing a northing, easting, elevation and handle. """
    def __init__(self, northing=0.0, easting=0.0, elevation=0.0, handle=None):
        self.northing = northing
        self.easting = easting
        self.elevation = elevation
        self.handle = new_handle(handle)

    def __str__(self):
        return "{}, {}, {}".format(self.easting, self.northing, self.elevation)

    def __eq__(self, point):
        return True if self.northing == point.northing and \
            self.easting == point.easting and \
            self.elevation == point.elevation \
            else False

class Line:
    """ Line class containing a starting point, end point, potential center_point and handle. """
    def __init__(self, start=Point(), end=Point(),
                 center_point=None, handle=None):
        if center_point is not None and not self.is_valid_center_point(start, end, center_point):
            raise ValueError("Invalid center point on init.")
        self.start = start
        self.end = end
        self.center_point = center_point
        self.handle = new_handle(handle)

    @staticmethod
    def is_valid_center_point(start, end, center_point):
        """ Checks to see if the center_point is equadistant to the start and end point. """
        distance_to_start = Line(center_point, start).get_length()
        distance_to_end = Line(center_point, end).get_length()
        return True if distance_to_start == distance_to_end else False

    def get_length(self):
        """ Calculates the length of the line using the northing, easting and elevation. """
        northing_distance = self.end.northing - self.start.northing
        easting_distance = self.end.easting - self.start.easting
        elevation_distance = self.end.elevation - self.start.elevation
        return math.sqrt(math.pow(northing_distance, 2)
                         + math.pow(easting_distance, 2)
                         + math.pow(elevation_distance, 2))

class Polyline:
    """ A dictionary of lines with the handle as the key. """
    def __init__(self, handle=None, *lines):
        self.elements = {}
        self._last_line_handle = None
        for line in lines:
            self.append(line)
        self.handle = new_handle(handle)

    def append(self, line: Line):
        """ Appends a line to the polyline. """
        self.elements[line.handle] = (self._last_line_handle, len(self.elements) + 1)
        self._last_line_handle = line.handle
