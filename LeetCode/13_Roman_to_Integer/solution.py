class Solution:
    def romanToInt(self, s):
        
        res = 0
        s = ["a"]+list(s)
        for i in range(1,len(s)):
            if s[i]=="I":
                res += 1
            elif s[i]=="V":
                if s[i-1]=="I":
                    res += 3
                else:
                    res += 5
            elif s[i]=="X":
                if s[i-1]=="I":
                    res += 8
                else:
                    res += 10
            elif s[i]=="L":
                if s[i-1]=="X":
                    res += 30
                else:
                    res += 50
            elif s[i]=="C":
                if s[i-1]=="X":
                    res += 80
                else:
                    res += 100
            elif s[i]=="D":
                if s[i-1]=="C":
                    res += 300 
                else:
                    res += 500
            elif s[i]=="M":
                if s[i-1]=="C":
                    res += 800
                else:
                    res += 1000
        return res
        