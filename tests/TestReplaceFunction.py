# -*- coding: utf-8 -*-
"""
Test replaceing numbers
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
        return utils.compareResultByTimeTuplesAndFlags(result, check, **kwargs)

    def setUp(self):
        self.cal = pdt.Calendar()
        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

    def testEnglishDates(self):
        start = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec).timetuple()

        target = datetime.datetime(
            self.yr, 9, 25, self.hr, self.mn, self.sec).timetuple()
        self.assertExpectedResult(
            self.cal.parse('twenty five september', start), (target, 1))

        target = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec) + datetime.timedelta(days=5)
        target = target.timetuple()
        self.assertExpectedResult(
            self.cal.parse('five days later', start), (target, 1))
        self.assertExpectedResult(
            self.cal.parse('next five days', start), (target, 1))

    def testFrenchNums(self):
        self.ptc = pdt.Constants('fr_FR', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'fr_FR':
            raise unittest.SkipTest(
                'Locale not set to fr_FR - check if PyICU is installed')

        start = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec).timetuple()

        target = datetime.datetime(
            self.yr, 9, 25, self.hr, self.mn, self.sec).timetuple()
        self.assertExpectedResult(
            self.cal.parse('vingt cinq septembre', start), (target, 1))

        target = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec) + datetime.timedelta(days=5)
        target = target.timetuple()
        self.assertExpectedResult(
            self.cal.parse('apres cinq jours', start), (target, 1))

    def testSpanishNums(self):
        self.ptc = pdt.Constants('es', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'es':
            raise unittest.SkipTest(
                'Locale not set to es - check if PyICU is installed')

        start = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec).timetuple()

        target = datetime.datetime(
            self.yr, 9, 25, self.hr, self.mn, self.sec).timetuple()
        self.assertExpectedResult(
            self.cal.parse('veinticinco de septiembre', start), (target, 1))


    def testGermanNums(self):
        self.ptc = pdt.Constants('de_DE', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'de_DE':
            raise unittest.SkipTest(
                'Locale not set to de_DE - check if PyICU is installed')

        start = datetime.datetime(
            self.yr, self.mth, self.dy, self.hr, self.mn, self.sec).timetuple()

        target = datetime.datetime(
            self.yr, 9, 25, self.hr, self.mn, self.sec).timetuple()
        self.assertExpectedResult(
            self.cal.parse('fünfundzwanzig September', start), (target, 1))



if __name__ == "__main__":
    unittest.main()