#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_aggregate
----------------------------------

Tests for `tstoolbox` module.
"""

from unittest import TestCase
from pandas.util.testing import assert_frame_equal
import shlex
import subprocess

import pandas

from tstoolbox import tstoolbox
from tstoolbox import tsutils


class TestAggregate(TestCase):
    def setUp(self):
        ''' Setup
        '''
        dr = pandas.date_range('2011-01-01', periods=2, freq='D')

        ts = pandas.Series([2, 2], index=dr)
        self.aggregate_direct_mean = pandas.DataFrame(ts,
                                                      columns=['Value_mean'])
        self.aggregate_direct_mean.index.name = 'Datetime'
        self.aggregate_direct_mean = tsutils.memory_optimize(self.aggregate_direct_mean)


        ts = pandas.Series([48, 48], index=dr)
        self.aggregate_direct_sum = pandas.DataFrame(ts, columns=['Value_sum'])
        self.aggregate_direct_sum.index.name = 'Datetime'
        self.aggregate_direct_sum = tsutils.memory_optimize(self.aggregate_direct_sum)

        self.aggregate_cli_mean = b"""Datetime,Value_mean
2011-01-01,2
2011-01-02,2
"""

        self.aggregate_cli_sum = b"""Datetime,Value_sum
2011-01-01,48
2011-01-02,48
"""

    def test_aggregate_direct_mean(self):
        ''' Test daily mean aggregation
        '''
        out = tstoolbox.aggregate(statistic='mean',
                                  agg_interval='daily',
                                  input_ts='tests/data_flat.csv')
        assert_frame_equal(out, self.aggregate_direct_mean)

    def test_aggregate_direct_sum(self):
        ''' Test daily mean summation
        '''
        out = tstoolbox.aggregate(statistic='sum',
                                  agg_interval='daily',
                                  input_ts='tests/data_flat.csv')
        assert_frame_equal(out, self.aggregate_direct_sum)

    def test_aggregate_cli_mean(self):
        ''' Test CLI mean, daily (by default) aggregation
        '''
        args = ('tstoolbox aggregate '
                '--statistic="mean" '
                '--input_ts="tests/data_flat.csv"')
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(out, self.aggregate_cli_mean)

    def test_aggregate_cli_sum(self):
        ''' Test CLI summation, daily (by default) aggregation
        '''
        args = ('tstoolbox aggregate '
                '--statistic="sum" '
                '--input_ts="tests/data_flat.csv"')
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(out, self.aggregate_cli_sum)
