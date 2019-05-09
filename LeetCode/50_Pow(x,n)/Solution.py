import math
class Solution:
    def myPow(self, x, n):
        if n==0:
            return 1
        if n > 0:
            pows=[x]
        else:
            pows=[1 / x]
            n *= -1
        cur_pow = 1
        tres = x
        
        while 2 * cur_pow <= n:
            tres *= tres
            cur_pow *=2
            pows.append(pows[-1] * pows[-1])
        
        index = 0
        res =1
        while n > 0:
            if n % 2 == 1:
                res *= pows[index]   
            index += 1
            n //= 2
        return res
                
                
        