class Solution:
    def addBinary(self, a, b):
        max_l = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        res = []
        curry = 0
        
        for i in range(max_l):
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[i]) if i < len(b) else 0
            res.append((curry + n1 + n2) % 2)
            curry =(curry + n1 + n2) // 2
            
        if curry > 0:
            res.append(curry)
            
        return "".join(map(str,res[::-1]))