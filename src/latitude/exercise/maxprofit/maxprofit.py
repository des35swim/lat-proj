
class Maxprofit(object):

    def __init__(self):
        self._max_diff = 0

    def calculate_max_profit(self, stock_prices):
        arr_size = len(stock_prices)
        max_diff = stock_prices[1] - stock_prices[0]
        min_element = stock_prices[0]
        
        # Loop through starting from 2nd element
        for i in range( 1, arr_size ):
            
            if (stock_prices[i] - min_element > max_diff):
                max_diff = stock_prices[i] - min_element
        
            if (stock_prices[i] < min_element):
                min_element = stock_prices[i]
        #endFor
        return max_diff
    #endDef


    def get_max_profit(self, stock_prices):
        max_profit = self.calculate_max_profit(stock_prices)
        return max_profit
    #endDef



# # Driver program to test above function
# stock_prices_yesterday = [10, 5, 6, 18, 10, 22, 5, 22]
# # size = len(prices)
# print ("Maximum difference is",
#         get_max_profit(stock_prices_yesterday))


# # get_max_profit(stock_prices_yesterday)