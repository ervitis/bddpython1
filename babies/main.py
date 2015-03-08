# -*- coding: utf-8 -*-

import sys
from content import Content
from babylist import Babies
import models


def main():
    filename = sys.argv[1:]

    if not filename:
        print 'Usage: <filename>.html'
        sys.exit(1)

    filename = filename[0]

    content_file = Content()
    if not content_file.initialize(filename):
        print 'Error reading file'
        sys.exit(1)

    year = content_file.get_year()
    content = content_file.get_table_content()
    if not year or not content:
        print 'Error getting the year or content'
        sys.exit(1)

    list_baby = Babies()
    list_baby.initialize(content=content, year=year)

    list_sorted = list_baby.sortlist()
    for baby in list_sorted:
        gender = 'male' if models.MALE == baby.gender else 'female'
        print baby.rank + ': ' + baby.name + ', gender: ' + gender

    print 'Total: ' + str(len(list_sorted))

    sys.exit(0)


if __name__ == '__main__':
    main()