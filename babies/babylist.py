# -*- coding: utf-8 -*-

from models import Baby, BabiesList
import models


class Babies():
    def __init__(self):
        self.babylist = BabiesList()

    def initialize(self, content, year):
        self.babylist.year = year

        for v in content:
            (rank, boyname, girlname) = v

            babygirl = Baby()
            babygirl.gender = models.FEMALE
            babygirl.name = girlname
            babygirl.rank = rank

            babyboy = Baby()
            babyboy.gender = models.MALE
            babyboy.name = boyname
            babyboy.rank = rank

            self.babylist.babies.append(babyboy)
            self.babylist.babies.append(babygirl)

    def sortlist(self):
        v = sorted(self.babylist.babies, key=lambda x: x.name, reverse=False)

        return v