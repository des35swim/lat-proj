import datetime  

class Maxprofit(object):

    def __init__(self):
        self._max_diff = 0

    def calculate_max_profit(self, stock_prices):
        arr_size = len(stock_prices)
        max_diff = stock_prices[1] - stock_prices[0]
        min_element = stock_prices[0]
        min_element_pos = 0
        max_element_pos = 0
        
        # Loop through starting from 2nd element
        for i in range( 1, arr_size ):
            
            if (stock_prices[i] - min_element > max_diff):
                max_diff = stock_prices[i] - min_element
                max_element_pos = i + 1
        
            if (stock_prices[i] < min_element):
                min_element = stock_prices[i]
                min_element_pos = i + 1
                
        #endFor
        return min_element_pos,max_element_pos,max_diff
    #endDef

    def get_yesterday_date(self):
        yesterday = datetime.date.today () - datetime.timedelta (days=1)
        t = datetime.time(hour=23, minute=30)
        print(datetime.datetime.combine(yesterday, t))        
    #endDef

    def get_buy_time(self, pos):
        # yesterday = datetime.date.today () - datetime.timedelta (days=1)
        open_trade_yesterday = datetime.time(day=-1, hour=10, minute=00)
        final_time = given_time + timedelta(minutes=n)
        final_time_str = final_time.strftime('%d/%m/%Y %H:%M:%S.%f')
        print("DEREK 1")
        print (final_time_str)
        return final_time_str
    #endDef

    def get_sell_time(self, pos, stock_prices):
        return stock_prices(pos)
    #endDef

    def get_max_profit(self, stock_prices):
        min_element_pos,max_element_pos,max_profit = self.calculate_max_profit(stock_prices)
        print "derek 1 " + str(min_element_pos)
        print "derek 2 " + str(max_element_pos)
        print "derek 3 " + str(max_profit)
        buy_time = self.get_buy_time(min_element_pos)
        return max_profit
    #endDef

# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

# # Driver program to test above function
# stock_prices_yesterday = [10, 5, 6, 18, 10, 22, 5, 22]
# # size = len(prices)
# print ("Maximum difference is",
#         get_max_profit(stock_prices_yesterday))


# # get_max_profit(stock_prices_yesterday)