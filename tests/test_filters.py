#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_peak_detect
----------------------------------

Tests for `tstoolbox` module.
"""

from __future__ import print_function

from pandas.util.testing import TestCase
from pandas.util.testing import assert_frame_equal
from pandas.util.testing import assertRaisesRegexp
import os

import shlex
import subprocess

import pandas as pd

from tstoolbox import tstoolbox
from tstoolbox import tsutils

test_sinwave = '''Datetime,0,0_peak,0_valley
2000-01-01 00:00:00,0.0,,
2000-01-01 01:00:00,0.258819045103,,
2000-01-01 02:00:00,0.5,,
2000-01-01 03:00:00,0.707106781187,,
2000-01-01 04:00:00,0.866025403784,,
2000-01-01 05:00:00,0.965925826289,,
2000-01-01 06:00:00,1.0,1.0,
2000-01-01 07:00:00,0.965925826289,,
2000-01-01 08:00:00,0.866025403784,,
2000-01-01 09:00:00,0.707106781187,,
2000-01-01 10:00:00,0.5,,
2000-01-01 11:00:00,0.258819045103,,
2000-01-01 12:00:00,1.22464679915e-16,,
2000-01-01 13:00:00,-0.258819045103,,
2000-01-01 14:00:00,-0.5,,
2000-01-01 15:00:00,-0.707106781187,,
2000-01-01 16:00:00,-0.866025403784,,
2000-01-01 17:00:00,-0.965925826289,,
2000-01-01 18:00:00,-1.0,,-1.0
2000-01-01 19:00:00,-0.965925826289,,
2000-01-01 20:00:00,-0.866025403784,,
2000-01-01 21:00:00,-0.707106781187,,
2000-01-01 22:00:00,-0.5,,
2000-01-01 23:00:00,-0.258819045103,,
'''

class TestFilter(TestCase):
    def setUp(self):
        self.ats = tstoolbox.read(os.path.join('tests', 'data_sine.csv'))
        self.ats.index.name = 'Datetime'
        self.ats.columns = ['Value']

        self.flat_3 = self.ats.join(tstoolbox.read(os.path.join('tests', 'data_filter_flat.csv')))

        self.hanning = self.ats.join(tstoolbox.read(os.path.join('tests', 'data_filter_hanning.csv')))

        self.fft_lowpass = self.ats.join(tstoolbox.read(os.path.join('tests', 'data_filter_fft_lowpass.csv')))

        self.fft_highpass = self.ats.copy()
        self.fft_highpass.columns = ['Value_filter']
        self.fft_highpass = self.ats.join(self.fft_highpass)

    def test_filter_flat(self):
        out = tstoolbox.filter('flat',
                               input_ts='tests/data_sine.csv',
                               print_input=True)
        self.maxDiff = None
        assert_frame_equal(out, self.flat_3)

    def test_filter_hanning(self):
        out = tstoolbox.filter('hanning',
                               input_ts='tests/data_sine.csv',
                               print_input=True)
        print(out)
        self.maxDiff = None
        assert_frame_equal(out, self.hanning)

    def test_filter_fft_lowpass(self):
        out = tstoolbox.filter('fft_lowpass',
                               input_ts='tests/data_sine.csv',
                               print_input=True,
                               cutoff_period=50)
        self.maxDiff = None
        assert_frame_equal(out, self.fft_lowpass)
#
#    def test_filter_fft_highpass(self):
#        out = tstoolbox.filter('fft_highpass',
#                               input_ts='tests/data_sine.csv',
#                               print_input=True,
#                               cutoff_period=12)
#        self.maxDiff = None
#        assert_frame_equal(out, self.fft_highpass)
#
#    def test_filter_flat_cli(self):
#        args = "tstoolbox filter flat --input_ts='tests/data_sine.csv' --print_input"
#        args = shlex.split(args)
#        out = subprocess.Popen(args,
#            stdout=subprocess.PIPE,
#            stdin=subprocess.PIPE).communicate(input=os.path.join('tests', 'data_sine.csv'))[0]
#        self.maxDiff = None
#        self.assertEqual(out, self.flat_3)
#
#    def test_filter_hanning_cli(self):
#        args = ('tstoolbox filter  hanning '
#                '--input_ts=self.ats, '
#                '--print_input=True)')
#        args = shlex.split(args)
#        out = subprocess.Popen(args,
#            stdout=subprocess.PIPE,
#            stdin=subprocess.PIPE).communicate(input=self.ats_cli)[0]
#        self.maxDiff = None
#        self.assertEqual(out, test_sinwave)
