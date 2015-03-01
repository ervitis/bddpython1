# -*- coding: utf-8 -*-

from lettuce import step, world


world.f = None

@step(u'The file "baby[0-9]{4}.html"')
def test_get_file(step):
    import os

    directory = os.getcwd()
    world.f = open(directory + '../../resources/baby1990.html')