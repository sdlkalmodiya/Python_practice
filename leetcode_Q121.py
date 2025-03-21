# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left=0
        right=1
        while left<len(prices):
            if right==len(prices):
                left+=1
                right=left+1
            elif prices[right]-prices[left]>profit:
                profit=prices[right]-prices[left]
                right+=1
            else:
                right+=1
        return profit


        
