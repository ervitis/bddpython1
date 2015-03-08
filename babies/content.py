# -*- coding: utf-8 -*-

import os
import re

RESOURCES_DIR = os.getcwd() + '/../resources/'

SEARCH_PATTERN_YEAR = r'Popularity\sin\s\d{4}'
SEARCH_PATTERN_CONTENT = r'<td>(\d{1,4})</td><td>(\w+)</td><td>(\w+)</td>'


class Content():
    def __init__(self):
        self.f = None
        self.text = None

    def initialize(self, file_name):
        self.f = open(RESOURCES_DIR + file_name, 'rU')

        if not self.f:
            return False

        self.text = self.f.read()

        if not self.text:
            return False

        return True

    def get_year(self):
        return self._get_year_match()

    def get_table_content(self):
        return self._get_content_match()

    def _get_year_match(self):
        year_match = re.search(SEARCH_PATTERN_YEAR, self.text)

        if not year_match:
            return False

        try:
            return int(year_match.group(0)[-4:])
        except Exception, e:
            return False

    def _get_content_match(self):
        content_match = re.findall(SEARCH_PATTERN_CONTENT, self.text)

        if not content_match:
            return False

        return set(content_match)