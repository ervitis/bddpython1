# -*- coding: utf-8 -*-

from unittest2 import TestCase
import os


class GetFile(TestCase):
    def setUp(self):
        self.current_directory = os.getcwd()
        self.f = None

    def open_file(self):
        self.assertRaises(IOError, open, self.current_directory)