class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for elem in nums:
            if elem != 0:
                nums[cur] = elem
                cur += 1
        nums[cur:] = [0] * (len(nums) - cur)