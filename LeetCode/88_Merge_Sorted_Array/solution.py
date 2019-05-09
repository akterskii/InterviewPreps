class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            min_el = nums2[0] - 1
        else:
            min_el = min(nums1[0], nums2[0]) - 1
        i1 = m - 1
        i2 = n - 1
        index = m + n - 1
        
        while index >= 0:
            if i1 >= 0:
                el1 = nums1[i1]
            else:
                el1 = min_el
            if i2 >= 0:
                el2 = nums2[i2]
            else:
                el2 = min_el
            if el1 >= el2:
                nums1[index] = el1
                i1 -= 1
            else:
                nums1[index] = el2
                i2 -= 1
            index -= 1