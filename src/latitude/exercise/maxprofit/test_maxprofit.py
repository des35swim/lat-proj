import sys

from maxprofit import Maxprofit

try:
    if sys.version_info < (2, 7):
        import unittest2
    else:
        raise ImportError()
except ImportError:
    import unittest

FAILURE = 'incorrect value'


class MaxprofitTest(unittest.TestCase):
    def setUp(self):
        self.maxprof = Maxprofit()

    def test_trade_time_1(self):
        value = self.maxprof.get_trade_time(22)
        self.assertEqual(value, "10:22", FAILURE)

    def test_trade_time_2(self):
        value = self.maxprof.get_trade_time(183)
        self.assertEqual(value, "13:03", FAILURE)

    def test_some_random_prices(self):
        stock_prices_yesterday = [10, 5, 6, 18, 10, 22, 5, 22]
        value = self.maxprof.get_max_profit(stock_prices_yesterday)
        self.assertEqual(value, ['10:02', '10:06', 17], FAILURE)

    def test_no_price_change(self):
        stock_prices_yesterday = [10, 10, 10]
        value = self.maxprof.get_max_profit(stock_prices_yesterday)
        self.assertEqual(value, ['10:00', '10:00', 0], FAILURE)

    def test_negative_profit(self):
        stock_prices_yesterday = [22, 20, 19, 18, 15]
        value = self.maxprof.get_max_profit(stock_prices_yesterday)
        self.assertEqual(value, ['10:05', '10:03', -1], FAILURE)
