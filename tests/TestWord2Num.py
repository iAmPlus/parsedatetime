# -*- coding: utf-8 -*-
"""
Test parsing of numbers written out in German, French, English and Spanish
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
        '''self.ptc = pdt.Constants('es', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'es':
            raise unittest.SkipTest(
                'Locale not set to es - check if PyICU is installed')'''
        self.cal = pdt.Calendar()
        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()
    def testEnglishNums(self):
        self.assertExpectedResult(
            self.cal.word_to_num('one hundred and forty seven'), 147)
        self.assertExpectedResult(
            self.cal.word_to_num('sixteen'), 16)
        self.assertExpectedResult(
            self.cal.word_to_num('seven'), 7)
        self.assertExpectedResult(
            self.cal.word_to_num('hundred and one'), 101)
        self.assertExpectedResult(
            self.cal.word_to_num('eighty five'), 85)
        self.assertExpectedResult(
            self.cal.word_to_num('sixty seven'), 67)
        self.assertExpectedResult(
            self.cal.word_to_num('in a week'), 1)

    def testFrenchNums(self):
        self.ptc = pdt.Constants('fr_FR', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'fr_FR':
            raise unittest.SkipTest(
                'Locale not set to fr_FR - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.word_to_num('quatre vingt dix huit'), 98)
        self.assertExpectedResult(
            self.cal.word_to_num('soixante quatorze'), 74)
        self.assertExpectedResult(
            self.cal.word_to_num('seize'), 16)
        self.assertExpectedResult(
            self.cal.word_to_num('vingt et un'), 21)
        self.assertExpectedResult(
            self.cal.word_to_num('cent soixante quatorze'), 174)
        self.assertExpectedResult(
            self.cal.word_to_num('deux cent soixante quatorze'), 274)
        self.assertExpectedResult(
            self.cal.word_to_num('cent un'), 101)
        self.assertExpectedResult(
            self.cal.word_to_num('quatre vingts'), 80)
        self.assertExpectedResult(
            self.cal.word_to_num('quatre vingt huit'), 88)
        self.assertExpectedResult(
            self.cal.word_to_num('quatre vingt seize'), 96)
        self.assertExpectedResult(
            self.cal.word_to_num('soixante dix'), 70)
        self.assertExpectedResult(
            self.cal.word_to_num('soixante dix huit'), 78)
        self.assertExpectedResult(
            self.cal.word_to_num('quatre vingt dix'), 90)

    def testSpanishNums(self):
        self.ptc = pdt.Constants('es', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'es':
            raise unittest.SkipTest(
                'Locale not set to es - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.word_to_num('noventa y ocho'), 98)
        self.assertExpectedResult(
            self.cal.word_to_num('setenta'), 70)
        self.assertExpectedResult(
            self.cal.word_to_num('veintisiete'), 27)
        self.assertExpectedResult(
            self.cal.word_to_num('uno'), 1)
        self.assertExpectedResult(
            self.cal.word_to_num('ciento veintitres'), 123)
        self.assertExpectedResult(
            self.cal.word_to_num('doscientos cuarenta y tres'), 243)
        self.assertExpectedResult(
            self.cal.word_to_num('ciento uno'), 101)
        self.assertExpectedResult(
            self.cal.word_to_num('doscientos setenta y seis'), 276)

    def testGermanNums(self):
        self.ptc = pdt.Constants('de_DE', usePyICU=False)
        self.cal = pdt.Calendar(self.ptc)

        (self.yr, self.mth, self.dy, self.hr,
         self.mn, self.sec, self.wd, self.yd, self.isdst) = time.localtime()

        if self.ptc.localeID != 'de_DE':
            raise unittest.SkipTest(
                'Locale not set to de_DE - check if PyICU is installed')

        self.assertExpectedResult(
            self.cal.word_to_num('einhundertundeins'), 101)
        self.assertExpectedResult(
            self.cal.word_to_num('einunddreibig'), 31)
        self.assertExpectedResult(
            self.cal.word_to_num('einhunderteinunddreibig'), 131)
        self.assertExpectedResult(
            self.cal.word_to_num('vierhundertelf'), 411)
        self.assertExpectedResult(
            self.cal.word_to_num('zweihundertzehn'), 210)
        self.assertExpectedResult(
            self.cal.word_to_num('neunzehn'), 19)



if __name__ == "__main__":
    unittest.main()