'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0

        min_so_far = 10e+05
        max_diff = -10e+05
        
        for i in range(len(prices)):
            max_diff = max(max_diff, prices[i]-min_so_far)
            if prices[i]<min_so_far:
                min_so_far = prices[i]
        if max_diff<0:
            max_diff = 0
        return max_diff
        

    def maxProfit_soln2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0

        # using two arrays to store max from right and min from left
        max_arr = [x for x in prices]
        min_arr = [x for x in prices]

        for i in range(1,len(prices)):
            j = len(prices)-i-1
            max_arr[j] = max(max_arr[j+1],prices[j])
            min_arr[i] = min(min_arr[i-1],prices[i])
        
        max_diff = -10e+05
        for i in range(len(prices)-1):
            diff = max_arr[i+1]-min_arr[i]
            if diff>=max_diff:
                max_diff = diff
        
        if max_diff<0:
            max_diff = 0
        return max_diff
