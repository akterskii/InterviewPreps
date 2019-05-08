"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        max_ = 0
        arr = []
        for inter in intervals:
            arr.append([inter.start, 1])
            arr.append([inter.end, -1])
        arr.sort()
        cur = 0
        for el in arr:
            # print(el, cur)
            cur += el[1]
            if cur > max_:
                max_ = cur
        return max_