#!/usr/bin/python
""" Unit tests for objects.py """
import collections
import exceptions
import objects
import unittest
import uuid
# Test all point values with point 0 or UTM coords of: 31 S 483925 2010789
#                                                      elev = 3918.63517

class Test_Functions(unittest.TestCase):
    def test_new_handle(self):
        handle = objects.new_handle()
        tested_handle = str(uuid.UUID(handle, version=4))
        self.assertEqual(handle, tested_handle)

    def test_new_handle_from_good_handle(self):
        good_handle = "6b341a83-6409-48a0-a917-22f27c8dfb30"
        self.assertEqual(good_handle, objects.new_handle(good_handle))

    def test_new_handle_from_bad_handle(self):
        bad_handle = "handles-are-for-the-weak"
        self.assertNotEqual(bad_handle, objects.new_handle(bad_handle))

class Test_Point_Class(unittest.TestCase):
    def test_point_init_as_empty(self):
        point = objects.Point()
        self.assertEqual(point.northing, 0)
        self.assertEqual(point.easting, 0)
        self.assertEqual(point.elevation, 0)

    def test_point_init_from_values(self):
        northing = 2010789
        easting = 483925
        elevation = 3918.63517
        point = objects.Point(northing, easting, elevation)
        self.assertEqual(point.northing, northing) 
        self.assertEqual(point.easting, easting)
        self.assertEqual(point.elevation, elevation)

    def test_point_str(self):
        point = objects.Point(2010789, 483925, 3918.63517)
        self.assertEqual(str(point), "483925, 2010789, 3918.63517") 

class Test_Line_Class(unittest.TestCase):
    def test_line_init_with_invalid_center_point(self):
        with self.assertRaises(exceptions.InvalidCenterPoint):
            line = objects.Line(objects.Point(1,1,1), objects.Point(-1,-1,-1),
                                objects.Point(2010789, 483925, 3918.63517))

    def test_line_init_as_empty(self):
        line = objects.Line()
        self.assertEqual(str(line.start), "0.0, 0.0, 0.0")
        self.assertEqual(str(line.end), "0.0, 0.0, 0.0")
        self.assertIsNone(line.center_point, None)

    def test_line_init_from_points(self):
        start_point = objects.Point()
        end_point = objects.Point(2010789, 483925, 3918.63517)
        line = objects.Line(start_point, end_point)
        self.assertEqual(line.start.handle, start_point.handle)
        self.assertEqual(line.end.handle, end_point.handle)
        self.assertEqual(line.center_point, None)

    def test_line_get_length(self):
        line = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        self.assertEqual(line.get_length(), 2068204.8167064101) 

    def test_line_is_valid_center_point(self):
        is_valid = objects.Line.is_valid_center_point(objects.Point(1,1,1),
                                                      objects.Point(-1,-1,-1),
                                                      objects.Point(0,0,0))
        self.assertEqual(is_valid, True)

    def test_line_is_invalid_center_point(self):
        is_invalid = objects.Line.is_valid_center_point(objects.Point(1,1,1),
                                                      objects.Point(-1,-1,-1),
                                                      objects.Point(2010789, 483925, 3918.63517))
        self.assertEqual(is_invalid, False)

if __name__ == '__main__':
    unittest.main()
