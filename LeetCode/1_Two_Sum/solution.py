class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d ={}
        for i,n in enumerate(nums):
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)
                
        for n in d:
            if target - n in d:
                if target - n == n:
                    if len(d[n]) > 1:
                        return [d[n][0], d[n][1]]
                else:
                    return [d[n][0], d[target - n][0]] 