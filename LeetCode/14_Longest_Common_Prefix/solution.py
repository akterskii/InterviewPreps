class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        cur = strs[0]
        
        for i in range(1,len(strs)):
            if len(cur) == 0:
                return ""
            good = 0
            for ls in zip(cur, strs[i]):
                if ls[0] == ls[1]:
                    good += 1
                else:
                    break
            cur = cur[:good]
                        
        return cur