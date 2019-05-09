class Solution:
    def countAndSay(self, n):
        def next(l):
            index = 1
            cur = l[0]
            cur_amount = 1
            res = []
            while index<len(l):
                if l[index]==cur:
                    cur_amount +=1
                else:
                    res=res+[cur_amount,cur]
                    cur = l[index]
                    cur_amount = 1
                index += 1
            res=res+[cur_amount,cur]
            return res
        counter = 1
        seq = [1]
        while counter<n:
            seq = next(seq)
            counter+=1
        return "".join(map(str,seq))
            
        