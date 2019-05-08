class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_ = {}
        num = 0
        for i in nums:
            if i in dict_:
                dict_[i][1] += 1
            else:
                dict_[i] = [num, 1]
                num += 1
        
        res = []
        for i in dict_:
            for j in dict_:
                if -i-j in dict_ and dict_[i][0] <= dict_[j][0] and dict_[j][0] <= dict_[-i-j][0]:
                    a,b,c = sorted([i,j,-i-j])
                    flag= False
                    if a<b<c:
                        flag=True
                    if a==b and b!=c and dict_[a][1]>1:
                        flag= True
                    if a!=b and b==c and dict_[b][1]>1:
                        flag= True
                    if a==b and b==c and dict_[a][1]>2:
                        flag= True
                    if flag:
                        res.append([a,b,c])
        return res