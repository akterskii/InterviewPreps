class Solution:
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        nums = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        amount = 1
        for n in digits:
            amount *= len(nums[int(n) - 2])
            
        cur =[0] * len(digits)
        res = []
        for i in range(amount):
            cur_list = []
            for i in range(len(digits)):
                if cur[i] == len(nums[int(digits[i])-2]):
                    cur[i] = 0
                    cur[i + 1] += 1
                cur_list.append(nums[int(digits[i]) - 2][cur[i]]) 
            res.append("".join(cur_list))
            cur[0] += 1
        return res
