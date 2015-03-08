# -*- coding: utf-8 -*-

MALE = 'm'
FEMALE = 'f'


class Baby():
    def __init__(self):
        self.rank = 0
        self.name = None
        self.gender = None


class BabiesList():
    def __init__(self):
        self.babies = []
        self.year = None