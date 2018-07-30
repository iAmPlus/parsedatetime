# -*- coding: utf-8 -*-
"""
Test parsing of numbers written out in dates
"""
from __future__ import unicode_literals

import sys
import time
import datetime
import parsedatetime as pdt
from . import utils

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class test(unittest.TestCase):

    @utils.assertEqualWithComparator
    def assertExpectedResult(self, result, check, **kwargs):
        return result == check

    def setUp(self):
        self.cal = pdt.Calendar()
        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

    def testEnglishDates(self):
        start = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec).timetuple()

        self.assertExpectedResult(
            self.cal.replaceNumber('twenty five september 2006'), ('25 september 2006'))

    def testFrenchNums(self):
        self.ptc = pdt.Constants('fr_FR', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'fr_FR':
            raise unittest.SkipTest(
                'Locale not set to fr_FR - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.replaceNumber('vingt cinq septembre 2006'), ('25 septembre 2006'))

    def testSpanishNums(self):
        self.ptc = pdt.Constants('es', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'es':
            raise unittest.SkipTest(
                'Locale not set to es - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.replaceNumber('veinticinco septiembre 2006'), ('25 septiembre 2006'))

    def testGermanNums(self):
        self.ptc = pdt.Constants('de_DE', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'de_DE':
            raise unittest.SkipTest(
                'Locale not set to de_DE - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.replaceNumber('funfundzwanzig september 2006'), ('25 september 2006'))

if __name__ == "__main__":
    unittest.main()