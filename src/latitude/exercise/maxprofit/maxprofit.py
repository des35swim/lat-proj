import time
from datetime import datetime, date, time, timedelta

class Maxprofit(object):

    def __init__(self):
        self._profit = 0
    #endDef

    def main(self, file_path):
        text_file = open(file_path, "r")
        stock_prices_yesterday = text_file.read().strip().split(',')
        for i in range(0, len(stock_prices_yesterday)):
            stock_prices_yesterday[i] = int(stock_prices_yesterday[i])
        #endFor

        maxprof = Maxprofit()
        value = maxprof.get_max_profit(stock_prices_yesterday)
        print (value)
    #endDef


    #############################################################
    # Returns an Array [<buy_time>,<sell_time>,<profit>]
    #############################################################
    def get_max_profit(self, stock_prices):
        # Initialize
        arr_size = len(stock_prices)
        profit = stock_prices[1] - stock_prices[0]
        min_element = stock_prices[0]
        min_element_pos = 0
        max_element_pos = 0
        
        # Loop through starting from 2nd element
        for i in range( 1, arr_size ):
            
            if (stock_prices[i] - min_element > profit):
                profit = stock_prices[i] - min_element
                max_element_pos = i + 1
        
            if (stock_prices[i] < min_element):
                min_element = stock_prices[i]
                min_element_pos = i + 1
        #endFor

        # Get the trade buy and sell times
        buy_time = self.get_trade_time(min_element_pos)
        sell_time = self.get_trade_time(max_element_pos)

        return [buy_time,sell_time,profit]
    #endDef


    #############################################################
    # Returns the trade time as a timestamp
    #############################################################
    def get_trade_timestamp(self, pos):
        yesterday = date.today() - timedelta(days = 1)
        open_trade_time = time(hour=10, minute=00)
        open_trade_yesterday = datetime.combine(yesterday, open_trade_time)

        trade_time = open_trade_yesterday + timedelta(minutes=pos)
        return(trade_time)
    #endDef


    #############################################################
    # Returns the trade time as a string HH:MM
    #############################################################
    def get_trade_time(self, pos):
        trade_time = self.get_trade_timestamp(pos)
        time_str = str(trade_time.hour).zfill(2) + ":" + str(trade_time.minute).zfill(2)
        return time_str
    #endDef
