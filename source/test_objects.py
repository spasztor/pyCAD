#!/usr/bin/python
""" Unit tests for objects.py """
import collections
import exceptions
import objects
import unittest
import uuid
# Test all point values with point 0 or UTM coords of: 31 S 483925 2010789
#                                                      elev = 3918.63517

class TestFunctions(unittest.TestCase):
    def test_new_handle(self):
        handle = objects.new_handle()
        tested_handle = str(uuid.UUID(handle, version=4))
        self.assertEqual(handle, tested_handle)

    def test_new_handle_from_good_handle(self):
        good_handle = "6b341a83-6409-48a0-a917-22f27c8dfb30"
        self.assertEqual(good_handle, objects.new_handle(good_handle))

    def test_new_handle_from_bad_handle(self):
        with self.assertRaises(ValueError):
            bad_handle = "handles-are-for-the-weak"
            objects.new_handle(bad_handle)

    def test_new_handle_from_none(self):
        no_handle = None
        self.assertNotEqual(no_handle, objects.new_handle(no_handle))

class TestPointClass(unittest.TestCase):
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

    def test_point_eq_true(self):
        point = objects.Point(2010789, 483925, 3918.63517)
        point_equal = objects.Point(2010789, 483925, 3918.63517)
        self.assertEqual(point, point_equal)

    def test_point_eq_false(self):
        point = objects.Point(2010789, 483925, 3918.63517)
        point_no_elevation = objects.Point(2010789, 483925, 0)
        point_no_northing = objects.Point(0, 483925, 3918.63517)
        point_no_easting = objects.Point(2010789, 0, 3918.63517)
        point_all_bad = objects.Point(0, 0, 0)
        is_no_elevation = point == point_no_elevation
        is_no_northing = point == point_no_northing
        is_no_easting = point == point_no_easting
        is_all_bad = point == point_all_bad

        self.assertEqual(is_no_elevation, False)
        self.assertEqual(is_no_northing, False)
        self.assertEqual(is_no_easting, False)
        self.assertEqual(is_all_bad, False)

    def test_point_ne_true(self):
        point = objects.Point(2010789, 483925, 3918.63517)
        point_no_elevation = objects.Point(2010789, 483925, 0)
        point_no_northing = objects.Point(0, 483925, 3918.63517)
        point_no_easting = objects.Point(2010789, 0, 3918.63517)
        point_all_bad = objects.Point(0, 0, 0)

        self.assertNotEqual(point, point_no_elevation)
        self.assertNotEqual(point, point_no_northing)
        self.assertNotEqual(point, point_no_easting)
        self.assertNotEqual(point, point_all_bad)

    def test_point_ne_false(self):
        point = objects.Point(2010789, 483925, 3918.63517)
        point_equal = objects.Point(2010789, 483925, 3918.63517)
        is_not_equal = point != point_equal
        self.assertEqual(is_not_equal, False)

class TestLineClass(unittest.TestCase):
    def test_line_init_with_invalid_center_point(self):
        with self.assertRaises(ValueError):
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

    def test_line_eq_true(self):
        line = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        line_equal = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        self.assertEqual(line, line_equal)

    def test_line_eq_false(self):
        line = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        line_differant_start = objects.Line(objects.Point(1,0,0),
                                            objects.Point(2010789, 483925, 3918.63517))
        line_differant_end = objects.Line(objects.Point(),
                                          objects.Point(2010789, 483924, 3918.63517))
        #line_differant_second_point = objects.Line(objects.Point(),
        #                                           objects.Point(2010789, 483924, 3918.63517),
        #                                           objects.Point(1,1,0))
        line_all_bad = objects.Line(objects.Point(0,1,0),
                                    objects.Point(0,2,0)) #Will have to test for second point.
        is_differant_start = line == line_differant_start
        is_differant_end = line == line_differant_end
        #is_differant_second_point = line == line_differant_second_point
        is_all_bad = line == line_all_bad

        self.assertEqual(is_differant_start, False)
        self.assertEqual(is_differant_end, False)
        #self.assertEqual(is_differant_second_point, False)
        self.assertEqual(is_all_bad, False)

    def test_line_ne_true(self):
        line = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        line_differant_start = objects.Line(objects.Point(1,0,0),
                                            objects.Point(2010789, 483925, 3918.63517))
        line_differant_end = objects.Line(objects.Point(),
                                          objects.Point(2010789, 483924, 3918.63517))
        #line_differant_second_point = objects.Line(objects.Point(),
        #                                           objects.Point(2010789, 483924, 3918.63517),
        #                                           objects.Point(1,1,0))
        line_all_bad = objects.Line(objects.Point(0,1,0),
                                    objects.Point(0,2,0)) #Will have to test for second point.

        self.assertNotEqual(line, line_differant_start)
        self.assertNotEqual(line, line_differant_end)
        #self.assertNotEqual(line, line_differant_second_point)
        self.assertNotEqual(line, line_all_bad)

    def test_line_ne_false(self):
        line = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        line_equal = objects.Line(objects.Point(),
                            objects.Point(2010789, 483925, 3918.63517))
        is_not_equal = line != line_equal
        self.assertEqual(is_not_equal, False)

class TestPolylineClass(unittest.TestCase):
    def test_init(self):
        line_1 = objects.Line(objects.Point(),
                              objects.Point(2010789, 483925, 3918.63517))
        line_2 = objects.Line(objects.Point(2010789, 483925, 3918.63517),
                              objects.Point())
        polyline = objects.Polyline([line_1, line_2])
        self.assertEqual(polyline.elements[line_1.handle], line_1)
        self.assertEqual(polyline.elements[line_2.handle], line_2)

    def test_append(self):
        pass

if __name__ == '__main__':
    unittest.main()
