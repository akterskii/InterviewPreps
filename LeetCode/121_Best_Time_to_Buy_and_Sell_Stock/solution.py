class Solution:
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        min_p = prices[0]
        best = 0
        for elem in prices[1:]:
            if elem<min_p:
                min_p = elem
            else:
                if elem - min_p >best:
                    best = elem - min_p
        return best