# -*- coding: utf-8 -*-

from unittest2 import TestCase
import os


class TestGetFile(TestCase):
    def setUp(self):
        self.current_directory = os.getcwd()
        self.f = self._get_file()

    def test_open_file(self):
        self.assertRaises(IOError, open, self.current_directory)

    def test_typeerror_file(self):
        self.current_directory += '/resources/baby1990.html'

        with open(self.current_directory, 'r') as self.f:
            self.assertRaises(TypeError, self.f)

        self.assertRaises(ValueError, open, self.current_directory, '4')

    def test_read_file(self):
        self.current_directory += '/resources/baby1990.html'
        f = open(self.current_directory, 'r')
        self.assertIsNotNone(f)

    def test_has_year(self):
        import re

        text = self.f.read()
        year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)

        self.assertIsNotNone(year)

        tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

        self.assertIsNotNone(tuples)
        self.assertEqual(len(tuples), 1000)

    def _get_file(self):
        return open(self.current_directory + '/resources/baby1990.html', 'rU')