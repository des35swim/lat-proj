# import sys

from latitude.exercise.maxprofit.maxprofit import Maxprofit
# from maxprofit import Maxprofit

stock_prices_yesterday = [10, 5, 6, 18, 10, 22, 5, 22]

maxprof = Maxprofit()
value = maxprof.get_max_profit(stock_prices_yesterday)
print (value)

