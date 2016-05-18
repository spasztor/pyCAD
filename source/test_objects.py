#!/usr/bin/python
""" Unit tests for objects.py """
import unittest
import objects
import uuid

class Test_objects(unittest.TestCase):
    def test_new_handle(self):
        """ Test for good output from objects.new_handle(). """
        handle = objects.new_handle()
        tested_handle = str(uuid.UUID(handle, version=4))
        self.assertEqual(handle, tested_handle)

    def test_new_handle_from_existing(self):
        """ Test for good output from objects.new_handle() from an existing good handle. """
        # Test with good handle:
        good_handle = "6b341a83-6409-48a0-a917-22f27c8dfb30"
        self.assertEqual(good_handle, objects.new_handle(good_handle))
        # Test with bad handle:
        bad_handle = "handles-are-for-the-weak"
        self.assertNotEqual(bad_handle, objects.new_handle(bad_handle))

    def test_point_init(self):
        """ Test the init for objects.point. """
        # Test with empty point
        point = objects.Point()
        self.assertEqual(point.northing, 0)
        self.assertEqual(point.easting, 0)
        self.assertEqual(point.elevation, 0)
        # Test with non-empty point at UTM coords of: 31 S 483925 2010789
        northing = 2010789
        easting = 483925
        elevation = 3918.63517
        point = objects.Point(northing, easting, elevation)
        self.assertEqual(point.northing, northing) 
        self.assertEqual(point.easting, easting)
        self.assertEqual(point.elevation, elevation)

    def test_line_init(self):
        """ Test the init for objects.line. """
        # Test with blank line
        line = objects.Line()
        self.assertEqual(line.start, objects.Point())
        self.assertEqual(line.end, objects.Point())
        self.assertIsNone(line.center_point, None)
        # Test with start and end points
        start_point = objects.Point()
        end_point = objects.Point(2010789, 483925, 3918.63517)
        line = objects.Line(start_point, end_point)
        self.assertEqual(line.start, start_point)
        self.assertEqual(line.end, end_point)
        self.assertEqual(line.center_point, None)

if __name__ == '__main__':
    unittest.main()
