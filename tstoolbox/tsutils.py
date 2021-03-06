"""A collection of functions used by tstoolbox, wdmtoolbox, ...etc."""

from __future__ import print_function
from __future__ import division

from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
import os
import sys
import gzip
import bz2
from io import StringIO
try:
    from fractions import gcd
except ImportError:
    from math import gcd
try:
    from functools import reduce
except ImportError:
    pass

try:
    from urllib.parse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pandas as pd
import numpy as np
from tabulate import tabulate as tb
from tabulate import simple_separated_format

docstrings = {
    'input_ts': r'''input_ts : str
        [optional, required if using Python API, default is '-' (stdin)]

        Whether from a file or standard input, data requires a first line
        header of column names.  Most separators will be automatically
        detected. Most common date formats can be used, but the closer to ISO
        8601 date/time standard the better.

        Command line::

            +-------------------------+------------------------+
            | --input_ts=filename.csv | to read 'filename.csv' |
            +-------------------------+------------------------+
            | --input_ts='-'          | to read from standard  |
            |                         | input (stdin).         |
            +-------------------------+------------------------+

            In many cases it is better to use redirection rather that use
            `--input_ts=filename.csv`.  The following are identical:

            From a file:

                command subcmd --input_ts=filename.csv

            From standard input:

                command subcmd --input_ts=- < filename.csv

            The BEST way since you don't have to include `--input_ts=-` because
            that is the default:

                command subcmd < filename.csv

            Can also combine commands by piping:

                command subcmd < filename.csv | command subcmd1 > fileout.csv

        As Python Library::

            You MUST use the `input_ts=...` option where `input_ts` can be one
            of a [pandas DataFrame, pandas Series, dict, tuple,
            list, StringIO, or file name].

            If result is a time series, returns a pandas DataFrame.
        ''',
    'columns': r'''columns
        [optional]

        Columns to select out of input.  Can use column names from the
        first line header or column numbers.  If using numbers, column
        number 1 is the first data column.  To pick multiple columns;
        separate by commas with no spaces. As used in `tstoolbox pick`
        command.''',
    'start_date': r'''start_date : str
        [optional]

        The start_date of the series in ISOdatetime format, or 'None'
        for beginning.''',
    'end_date': r'''end_date : str
        [optional]

        The end_date of the series in ISOdatetime format, or 'None' for
        end.''',
    'dropna': r'''dropna : str
        [optional, defauls it 'no']

        Set `dropna` to 'any' to have records dropped that have NA value
        in any column, or 'all' to have records dropped that have NA in
        all columns.  Set to 'no' to not drop any records.  The default
        is 'no'.''',
    'print_input': r'''print_input
        [optional, default is False]

        If set to 'True' will include the input columns in the output
        table.''',
    'round_index': r'''round_index
        [optional]

        Round the index to the nearest time point.  Can significantly
        improve the performance since can cut down on memory and
        processing requirements, however be cautious about rounding to
        a very course interval from a small one.  This could lead to
        duplicate values in the index.''',
    'float_format': r'''float_format
        [optional]

        Format for float numbers.''',
    'tablefmt': r'''tablefmt : str
        [optional, default is 'simple']

        The table format.  Can be one of 'cvs', 'tvs', 'plain',
        'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki', 'latex',
        'latex_raw' and 'latex_booktabs'.''',
    'header': r'''header : str
        [optional, default is 'default']

        This is if you want a different header than is the default for
        this table.  Pass a list of strings for each column in the
        table.''',
    'pandas_offset_codes': r'''+-------+-----------------------------+
        | Alias | Description                 |
        +=======+=============================+
        | B     | business day                |
        +-------+-----------------------------+
        | C     | custom business day         |
        |       | (experimental)              |
        +-------+-----------------------------+
        | D     | calendar day                |
        +-------+-----------------------------+
        | W     | weekly                      |
        +-------+-----------------------------+
        | M     | month end                   |
        +-------+-----------------------------+
        | BM    | business month end          |
        +-------+-----------------------------+
        | CBM   | custom business month end   |
        +-------+-----------------------------+
        | MS    | month start                 |
        +-------+-----------------------------+
        | BMS   | business month start        |
        +-------+-----------------------------+
        | CBMS  | custom business month start |
        +-------+-----------------------------+
        | Q     | quarter end                 |
        +-------+-----------------------------+
        | BQ    | business quarter end        |
        +-------+-----------------------------+
        | QS    | quarter start               |
        +-------+-----------------------------+
        | BQS   | business quarter start      |
        +-------+-----------------------------+
        | A     | year end                    |
        +-------+-----------------------------+
        | BA    | business year end           |
        +-------+-----------------------------+
        | AS    | year start                  |
        +-------+-----------------------------+
        | BAS   | business year start         |
        +-------+-----------------------------+
        | H     | hourly                      |
        +-------+-----------------------------+
        | T     | minutely                    |
        +-------+-----------------------------+
        | S     | secondly                    |
        +-------+-----------------------------+
        | L     | milliseconds                |
        +-------+-----------------------------+
        | U     | microseconds                |
        +-------+-----------------------------+
        | N     | nanoseconds                 |
        +-------+-----------------------------+

        Weekly has the following anchored frequencies:

        +-------+-------------------------------+
        | Alias | Description                   |
        +=======+===============================+
        | W-SUN | weekly frequency (sundays).   |
        |       | Same as 'W'.                  |
        +-------+-------------------------------+
        | W-MON | weekly frequency (mondays)    |
        +-------+-------------------------------+
        | W-TUE | weekly frequency (tuesdays)   |
        +-------+-------------------------------+
        | W-WED | weekly frequency (wednesdays) |
        +-------+-------------------------------+
        | W-THU | weekly frequency (thursdays)  |
        +-------+-------------------------------+
        | W-FRI | weekly frequency (fridays)    |
        +-------+-------------------------------+
        | W-SAT | weekly frequency (saturdays)  |
        +-------+-------------------------------+

        Quarterly frequencies (Q, BQ, QS, BQS) and annual frequencies
        (A, BA, AS, BAS) have the following anchoring suffixes:

        +-------+-------------------------------+
        | Alias | Description                   |
        +=======+===============================+
        | -DEC  | year ends in December (same   |
        |       | as 'Q' and 'A')               |
        +-------+-------------------------------+
        | -JAN  | year ends in January          |
        +-------+-------------------------------+
        | -FEB  | year ends in February         |
        +-------+-------------------------------+
        | -MAR  | year ends in March            |
        +-------+-------------------------------+
        | -APR  | year ends in April            |
        +-------+-------------------------------+
        | -MAY  | year ends in May              |
        +-------+-------------------------------+
        | -JUN  | year ends in June             |
        +-------+-------------------------------+
        | -JUL  | year ends in July             |
        +-------+-------------------------------+
        | -AUG  | year ends in August           |
        +-------+-------------------------------+
        | -SEP  | year ends in September        |
        +-------+-------------------------------+
        | -OCT  | year ends in October          |
        +-------+-------------------------------+
        | -NOV  | year ends in November         |
        +-------+-------------------------------+''',
    'plotting_position_table': r'''+------------+-----+-----------------+-----------------------+
        | Name       | a   | Equation        | Description           |
        |            |     | (1-a)/(n+1-2*a) |                       |
        +============+=====+=================+=======================+
        | weibull    | 0   | i/(n+1)         | mean of sampling      |
        |            |     |                 | distribution          |
        |            |     |                 | (default)             |
        +------------+-----+-----------------+-----------------------+
        | benard and | 0.3 | (i-0.3)/(n+0.4) | approx. median of     |
        | bos-       |     |                 | sampling distribution |
        | levenbach  |     |                 |                       |
        +------------+-----+-----------------+-----------------------+
        | tukey      | 1/3 | (i-1/3)/(n+1/3) | approx. median of     |
        |            |     |                 | sampling distribution |
        +------------+-----+-----------------+-----------------------+
        | gumbel     | 1   | (i-1)/(n-1)     | mode of sampling      |
        |            |     |                 | distribution          |
        +------------+-----+-----------------+-----------------------+
        | hazen      | 1/2 | (i-1/2)/n       | midpoints of n equal  |
        |            |     |                 | intervals             |
        +------------+-----+-----------------+-----------------------+
        | cunnane    | 2/5 | (i-2/5)/(n+1/5) | subjective            |
        +------------+-----+-----------------+-----------------------+
        | california | NA  | i/n             |                       |
        +------------+-----+-----------------+-----------------------+

        Where 'i' is the sorted rank of the y value, and 'n' is the
        total number of values to be plotted.'''
        }


def b(s):
    """Make sure strings are correctly represented in Python 2 and 3."""
    try:
        return s.encode("utf-8")
    except AttributeError:
        return s


def doc(fdict, **kwargs):
    """Return a decorator that formats a docstring."""
    def f(fn):
        fn.__doc__ = fn.__doc__.format(**fdict)
        for attr in kwargs:
            setattr(fn, attr, kwargs[attr])
        return fn
    return f


def parsedate(dstr,
              strftime=None,
              settings=None):
    """ Uses dateparser to parse a wide variety of dates for the
        toolboxes.  Used for start and end dates. """
    import dateparser
    import datetime

    # The API should boomerang a datetime.datetime instance and None.
    if isinstance(dstr, datetime.datetime):
        if strftime is None:
            return dstr
        else:
            return dstr.strftime(strftime)

    if dstr is None:
        return dstr

    pdate = dateparser.parse(dstr, settings=settings)

    if pdate is None:
        pdate = pd.to_datetime(dstr)

    if pdate is None:
        raise ValueError("""
*
*   Could not parse date string '{0}'.
*
""".format(dstr))

    if strftime is None:
        return pdate
    return pdate.strftime(strftime)


def about(name):
    """ This generic 'about' function is used across all toolboxes. """
    import platform
    import pkg_resources
    namever = str(pkg_resources.get_distribution(name.split(".")[0]))
    print("package name = {0}\npackage version = {1}".format(
        *namever.split()))

    print("platform architecture = {0}".format(platform.architecture()))
    print("platform machine = {0}".format(platform.machine()))
    print("platform = {0}".format(platform.platform()))
    print("platform processor = {0}".format(platform.processor()))
    print("platform python_build = {0}".format(platform.python_build()))
    print("platform python_compiler = {0}".format(platform.python_compiler()))
    print("platform python branch = {0}".format(platform.python_branch()))
    print("platform python implementation = {0}".format(
        platform.python_implementation()))
    print("platform python revision = {0}".format(platform.python_revision()))
    print("platform python version = {0}".format(platform.python_version()))
    print("platform release = {0}".format(platform.release()))
    print("platform system = {0}".format(platform.system()))
    print("platform version = {0}".format(platform.version()))


def _round_index(ntsd,
                 round_index=None):
    """ Rounds the index, typically time, to the nearest interval. """
    ntsd.index = ntsd.index.round(round_index)
    return ntsd


def common_kwds(input_tsd=None,
                start_date=None,
                end_date=None,
                pick=None,
                force_freq=None,
                groupby=None,
                dropna='no',
                round_index=None):
    """Collected all common_kwds across sub-commands into single function.

    Parameters
    ----------
    input_tsd: DataFrame
        Input data which should be a DataFrame.

    required: str, bytes, tuple of str or bytes, list
        If str or bytes then split on "," and represents column names in
        input_tsd.

    Returns
    -------
    df: DataFrame
        DataFrame altered according to options.
    """

    ntsd = input_tsd

    if pick is not None:
        ntsd = _pick(ntsd,
                     pick)

    if start_date is not None or end_date is not None:
        ntsd = _date_slice(ntsd,
                           start_date=parsedate(start_date),
                           end_date=parsedate(end_date))

    if force_freq is not None:
        ntsd = asbestfreq(ntsd,
                          force_freq=force_freq)

    if ntsd.index.is_all_dates is True:
        ntsd.index.name = 'Datetime'

    if groupby is not None:
        if groupby == 'months_across_years':
            return ntsd.groupby(lambda x: x.month)
        else:
            return ntsd.groupby(pd.TimeGrouper(groupby))

    if round_index is not None:
        return _round_index(ntsd,
                            round_index=round_index)

    if dropna not in ['any', 'all', 'no']:
        raise ValueError("""
*
*   The "dropna" option must be "any", "all" or "no", not "{0}".
*
""".format(dropna))

    if dropna in ['any', 'all']:
        ntsd.dropna(axis='index',
                    how=dropna,
                    inplace=True)
    else:
        try:
            ntsd = asbestfreq(ntsd)
        except ValueError:
            pass

    return ntsd


def _pick(tsd, columns):
    columns = columns.split(',')
    ncolumns = []

    for i in columns:
        if i in tsd.columns:
            # if using column names
            ncolumns.append(tsd.columns.tolist().index(i))
            continue
        elif i == tsd.index.name:
            # if wanting the index
            # making it -1 that will be evaluated later...
            ncolumns.append(-1)
            continue
        else:
            # if using column numbers
            try:
                target_col = int(i) - 1
            except ValueError:
                raise ValueError("""
*
*   The name {0} isn't in the list of column names
*   {1}.
*
""".format(i, tsd.columns))
            if target_col < 0:
                raise ValueError("""
*
*   The requested column index {0} must be greater than or equal to 0.
*   First data column is index 1, index is column 0.
*
""".format(i))
            if target_col > len(tsd.columns):
                raise ValueError("""
*
*   The request column index {0} must be less than the
*   number of columns {1}.
*
""".format(i, len(tsd.columns)))

            # columns names or numbers or index organized into
            # numbers in ncolumns
            ncolumns.append(target_col)

    if len(ncolumns) == 1 and ncolumns[0] != -1:
        return pd.DataFrame(tsd[tsd.columns[ncolumns]])

    newtsd = pd.DataFrame()
    for index, col in enumerate(ncolumns):
        if col == -1:
            # Use the -1 marker to indicate index
            jtsd = pd.DataFrame(tsd.index)
        else:
            jtsd = pd.DataFrame(tsd[tsd.columns[col]])

        newtsd = newtsd.join(jtsd,
                             lsuffix='_{0}'.format(index),
                             how='outer')
    return newtsd


def _date_slice(input_tsd,
                start_date=None,
                end_date=None):
    """Private function to slice time series."""
    if input_tsd.index.is_all_dates:
        accdate = []
        for testdate in [start_date, end_date]:
            if testdate is None:
                tdate = None
            else:
                tdate = pd.Timestamp(testdate)
                # Is this comparison cheaper than the .join?
                if not pd.np.any(input_tsd.index == tdate):
                    # Create a dummy column at the date I want, then delete
                    # Not the best, but...
                    row = pd.DataFrame([pd.np.nan], index=[tdate])
                    row.columns = ['deleteme']
                    input_tsd = input_tsd.join(row, how='outer')
                    input_tsd.drop('deleteme', inplace=True, axis=1)
            accdate.append(tdate)

        return input_tsd[slice(*accdate)]
    else:
        return input_tsd


_ANNUALS = {
    0: 'DEC',
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

_WEEKLIES = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}


def asbestfreq(data, force_freq=None):
    """Test to determine best frequency to represent data.

    This uses several techniques.
    0.5.  If index is not DateTimeIndex, return
    1. If force_freq is set use .asfreq.
    2. If data.index.freq is not None, just return.
    3. If data.index.inferred_freq is set use .asfreq.
    4. Use pd.infer_freq - fails if any missing
    5. Use .is_* functions to establish A, AS, A-*, AS-*, Q, QS, M, MS
    6. Use minimum interval to establish the fixed time periods up to weekly
    7. Gives up returning None for PANDAS offset string
    """
    if not isinstance(data.index, pd.DatetimeIndex):
        return data

    ndiff = (data.index.values.astype('int64')[1:] -
             data.index.values.astype('int64')[:-1])
    if np.any(ndiff == 0):
        raise ValueError("""
*
*   Duplicate index entry record {1} (start count at 0):
*   "{0}".
*
""".format(data.index[:-1][ndiff == 0][0], pd.np.where(ndiff == 0)[0][0] + 1))
    if np.any(ndiff < 0):
        raise ValueError("""
*
*   Time warp.  The datetime index is not sorted at
*   record {1} (start count at 0):
*   "{0}".
*
""".format(data.index[ndiff < 0][0], pd.np.where(ndiff < 0)[0][0] + 1))

    if force_freq is not None:
        return data.asfreq(force_freq)

    if data.index.freq is not None:
        return data

    # Since pandas doesn't set data.index.freq and data.index.freqstr when
    # using .asfreq, this function returns that PANDAS time offset alias code
    # also.  Not ideal at all.

    # This gets most of the frequencies...
    try:
        return data.asfreq(data.index.inferred_freq)
    except ValueError:
        pass

    # pd.infer_freq would fail if given a large dataset
    if len(data.index) > 100:
        slic = slice(None, 99)
    else:
        slic = slice(None, None)
    infer_freq = pd.infer_freq(data.index[slic])
    if infer_freq is not None:
        return data.asfreq(infer_freq)

    # At this point pd.infer_freq failed probably because of missing values.
    # The following algorithm would not capture things like BQ, BQS
    # ...etc.
    if np.alltrue(data.index.is_year_end):
        infer_freq = 'A'
    elif np.alltrue(data.index.is_year_start):
        infer_freq = 'AS'
    elif np.alltrue(data.index.is_quarter_end):
        infer_freq = 'Q'
    elif np.alltrue(data.index.is_quarter_start):
        infer_freq = 'QS'
    elif np.alltrue(data.index.is_month_end):
        if np.all(data.index.month == data.index[0].month):
            # Actually yearly with different ends
            infer_freq = 'A-{0}'.format(_ANNUALS[data.index[0].month])
        else:
            infer_freq = 'M'
    elif np.alltrue(data.index.is_month_start):
        if np.all(data.index.month == data.index[0].month):
            # Actually yearly with different start
            infer_freq = 'A-{0}'.format(_ANNUALS[data.index[0].month] - 1)
        else:
            infer_freq = 'MS'

    if infer_freq is not None:
        return data.asfreq(infer_freq)

    # Use the minimum of the intervals to test a new interval.
    # Should work for fixed intervals.
    ndiff = sorted(set(ndiff))
    mininterval = np.min(ndiff)
    if mininterval <= 0:
        raise ValueError
    if len(ndiff) == 1:
        ngcd = ndiff[0]
    else:
        ngcd = reduce(gcd, ndiff)
    if ngcd < 1000:
        infer_freq = '{0}N'.format(ngcd)
    elif ngcd < 1000000:
        infer_freq = '{0}U'.format(ngcd // 1000)
    elif ngcd < 1000000000:
        infer_freq = '{0}L'.format(ngcd // 1000000)
    elif ngcd < 60000000000:
        infer_freq = '{0}S'.format(ngcd // 1000000000)
    elif ngcd < 3600000000000:
        infer_freq = '{0}T'.format(ngcd // 60000000000)
    elif ngcd < 86400000000000:
        infer_freq = '{0}H'.format(ngcd // 3600000000000)
    elif ngcd < 604800000000000:
        infer_freq = '{0}D'.format(ngcd // 86400000000000)
    elif ngcd < 2419200000000000:
        infer_freq = '{0}W'.format(ngcd // 604800000000000)
        if np.all(data.index.dayofweek == data.index[0].dayofweek):
            infer_freq = infer_freq + '-{0}'.format(
                _WEEKLIES[data.index[0].dayofweek])
        else:
            infer_freq = 'D'

    if infer_freq is not None:
        return data.asfreq(infer_freq)

    # Give up
    return data


# Utility
def print_input(iftrue,
                intds,
                output,
                suffix,
                date_format=None,
                float_format='%g',
                tablefmt="csv",
                showindex="never"):
    """Used when wanting to print the input time series also."""
    if suffix:
        output.rename(columns=lambda xloc: str(xloc) + suffix, inplace=True)
    if iftrue:
        return printiso(intds.join(output,
                                   lsuffix='_1',
                                   rsuffix='_2',
                                   how='outer'),
                        date_format=date_format,
                        float_format=float_format,
                        tablefmt=tablefmt,
                        showindex=showindex)
    return printiso(output,
                    date_format=date_format,
                    float_format=float_format,
                    tablefmt=tablefmt,
                    showindex=showindex)


def _apply_across_columns(func, xtsd, **kwds):
    """Apply a function to each column in turn."""
    for col in xtsd.columns:
        xtsd[col] = func(xtsd[col], **kwds)
    return xtsd


def _printiso(tsd,
              date_format=None,
              sep=',',
              float_format='%g',
              showindex="never",
              headers="keys",
              tablefmt="csv"):
    """Separate so can use in tests."""
    sys.tracebacklimit = 1000

    if isinstance(tsd, (pd.DataFrame, pd.Series)):
        if isinstance(tsd, pd.Series):
            tsd = pd.DataFrame(tsd)

        if len(tsd.columns) == 0:
            tsd = pd.DataFrame(index=tsd.index)

        # Not perfectly true, but likely will use showindex for indices
        # that are not time stamps.
        if showindex is True:
            if not tsd.index.name:
                tsd.index.name = 'UniqueID'
        else:
            if not tsd.index.name:
                tsd.index.name = 'Datetime'

        print_index = True
        if tsd.index.is_all_dates is True:
            if tsd.index.name is None:
                tsd.index.name = 'Datetime'
            # Someone made the decision about the name
            # This is how I include time zone info by tacking on to the
            # index.name.
            elif 'datetime' not in tsd.index.name.lower():
                tsd.index.name = 'Datetime'
        else:
            # This might be overkill, but tstoolbox is for time-series.
            # Revisit if necessary.
            print_index = False

        if tsd.index.name == 'UniqueID':
            print_index = False

        if showindex in ['always', 'default']:
            print_index = True

    elif isinstance(tsd, (int, float, tuple, pd.np.ndarray)):
        tablefmt = None

    if tablefmt in ["csv", "tsv", "csv_nos", "tsv_nos"]:
        sep = {"csv": ",",
               "tsv": "\\t",
               "csv_nos": ",",
               "tsv_nos": "\\t"}[tablefmt]
        if isinstance(tsd, pd.DataFrame):
            try:
                tsd.to_csv(sys.stdout,
                           float_format=float_format,
                           date_format=date_format,
                           sep=sep,
                           index=print_index)
                return
            except IOError:
                return
        else:
            fmt = simple_separated_format(sep)
    else:
        fmt = tablefmt

    if fmt is None:
        print(str(list(tsd))[1:-1])
    elif tablefmt in ['csv_nos', 'tsv_nos']:
        print(tb(tsd,
                 tablefmt=fmt,
                 showindex=showindex,
                 headers=headers).replace(' ', ''))
    else:
        print(tb(tsd,
                 tablefmt=fmt,
                 showindex=showindex,
                 headers=headers))


def test_cli():
    """The structure to test the cli."""
    import traceback
    try:
        oldtracebacklimit = sys.tracebacklimit
    except AttributeError:
        oldtracebacklimit = 1000
    sys.tracebacklimit = 1000
    cli = False
    for i in traceback.extract_stack():
        if os.path.sep + 'mando' + os.path.sep in i[0] or 'baker' in i[0]:
            cli = True
            break
    sys.tracebacklimit = oldtracebacklimit
    return cli


def printiso(tsd,
             date_format=None,
             float_format='%g',
             tablefmt="csv",
             headers="keys",
             showindex="never"):
    """
    Default output format.

    Used for tstoolbox, wdmtoolbox, swmmtoolbox, and hspfbintoolbox.

    """

    if test_cli():
        _printiso(tsd,
                  float_format=float_format,
                  date_format=date_format,
                  tablefmt=tablefmt,
                  headers=headers,
                  showindex=showindex)
    else:
        if isinstance(tsd, pd.DataFrame):
            def rename_map(x):
                try:
                    return x.replace(',', '_').replace(' ', '_')
                except:
                    return x
            tsd.rename(columns=rename_map,
                       inplace=True)
        return tsd


def open_local(filein):
    """
    Open the given input file.

    It can decode various formats too, such as gzip and bz2.
    """
    ext = os.path.splitext(filein)[1]
    if ext in ['.gz', '.GZ']:
        return gzip.open(filein, 'rb')
    if ext in ['.bz', '.bz2']:
        return bz2.BZ2File(filein, 'rb')
    return open(filein, 'r')


def memory_optimize(tsd):
    # Convert all datetime columns to datetime objects
    tsd = tsd.apply(lambda col: pd.to_datetime(col,
                                               errors='ignore')
                    if col.dtypes == object else col, axis=0)
    tsd = tsd.apply(lambda col: pd.to_numeric(col,
                                              errors='ignore',
                                              downcast='float')
                    if col.dtypes == float else col, axis=0)
    tsd = tsd.apply(lambda col: pd.to_numeric(col,
                                              errors='ignore',
                                              downcast='integer')
                    if col.dtypes == int else col, axis=0)
    return tsd


def is_valid_url(url, qualifying=None):
    min_attributes = ('scheme', 'netloc')
    qualifying = min_attributes if qualifying is None else qualifying
    token = urlparse(url)
    return all([getattr(token, qualifying_attr)
                for qualifying_attr in qualifying])


def _convert_to_numbers(numstr):
    ret = []
    for each in numstr:
        try:
            ret.append(int(each))
        except ValueError:
            try:
                ret.append(float(each))
            except ValueError:
                ret.append(each)
    return ret


def read_iso_ts(indat,
                parse_dates=True,
                extended_columns=False,
                dropna=None,
                force_freq=None):
    """ Read the format printed by 'printiso' and maybe other formats.

    Parameters
    ----------
    indat: str, bytes, StringIO, file pointer, file name, DataFrame,
           Series, tuple, list, dict

        The input data.

    Returns
    -------
    df: DataFrame

        Returns a DataFrame.
    """

    if isinstance(indat, (str, bytes, StringIO)):
        lindat = b(indat).split(b(","))
        if indat == '-':
            # if from stdin format must be the tstoolbox standard
            # pandas read_table supports file like objects
            header = 0
            sep = ','
            fpi = sys.stdin
            fname = '_'
        elif isinstance(indat, StringIO):
            header = 'infer'
            sep = None
            fpi = indat
            fname = ''
        elif '\n' in b(indat).decode() or '\r' in b(indat).decode():
            # a string?
            header = 'infer'
            sep = None
            fpi = StringIO(b(indat).decode())
            fname = ''
        elif len(lindat) > 1:
            result = pd.DataFrame({'values': _convert_to_numbers(lindat)},
                                  index=list(range(len(lindat))))
            return result
        elif os.path.exists(indat):
            # a local file
            header = 'infer'
            sep = None
            fpi = open_local(indat)
            fname = os.path.splitext(os.path.basename(indat))[0]
        elif is_valid_url(indat):
            # a url?
            header = 'infer'
            sep = None
            fpi = indat
            fname = ''
        else:
            raise ValueError("""
*
*   Can't figure out what "input_ts={0}" is.
*   I tested if it was a string or StringIO object, DataFrame, local file,
*   or an URL.  If you want to pull from stdin use "-".
*
""".format(indat))

        fstr = '{1}'
        if extended_columns is True:
            fstr = '{0}.{1}'

        index_col = 0
        if parse_dates is False:
            index_col = False

        # Would want this to be more generic...
        na_values = []
        for spc in range(20)[1:]:
            spcs = ' ' * spc
            na_values.append(spcs)
            na_values.append(spcs + 'nan')

        result = pd.io.parsers.read_table(fpi,
                                          header=header,
                                          index_col=index_col,
                                          infer_datetime_format=True,
                                          parse_dates=True,
                                          na_values=na_values,
                                          keep_default_na=True,
                                          sep=sep,
                                          skipinitialspace=True,
                                          engine='python')
        result.columns = [fstr.format(fname, str(i).strip())
                          for i in result.columns]

    elif isinstance(indat, pd.DataFrame):
        result = indat

    elif isinstance(indat, (pd.Series, dict)):
        result = pd.DataFrame(indat)

    elif isinstance(indat, (tuple, list)):
        result = pd.DataFrame({'values': indat})

    elif isinstance(indat, (int, float)):
        result = pd.DataFrame({'value': indat}, index=[0])

    else:
        raise ValueError("""
*
*   Can't figure out what was passed to read_iso_ts.
*   You gave me {0}, of
*   {1}.
*
""".format(indat, type(indat)))

    result = memory_optimize(result)

    if result.index.is_all_dates is False:
        try:
            result.set_index(0, inplace=True)
        except KeyError:
            pass

    if result.index.is_all_dates is True:
        result.index.name = 'Datetime'

        if force_freq is not None:
            try:
                return asbestfreq(result, force_freq=force_freq)
            except ValueError:
                return result

    if dropna in [b('any'), b('all')]:
        result.dropna(how=dropna, inplace=True)

    return result


def read_excel_csv(fpi, header=None):
    """Read Excel formatted CSV file."""
    if header is not None:
        header = int(header)
    tsdata = pd.read_table(fpi, header=header, sep=',', parse_dates=[0],
                           index_col=[0])
    return tsdata
