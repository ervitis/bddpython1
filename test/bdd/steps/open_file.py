# -*- coding: utf-8 -*-

from lettuce import step, world
from nose import tools
import re

world.f = None
world.text = None


@step(u'The file "baby1990.html"')
def test_get_file(step):
    import os

    directory = os.getcwd()
    world.f = open(directory + '/resources/baby1990.html', 'rU')
    tools.assert_is_not_none(world.f)


@step(u'I read the file and get the table with the information')
def test_read_file(step):
    world.text = world.f.read()
    tools.assert_is_not_none(world.text)

    year = re.search(r'Popularity\sin\s\d{4}', world.text)
    tools.assert_is_not_none(year)

    year = int(year.group(0)[-4:])
    tools.assert_true(isinstance(year, int))

    lines = re.findall(r'<td>\d{1,4}</td><td>\w+</td><td>\w+</td>', world.text)
    tools.assert_equal(len(lines), 1000)
