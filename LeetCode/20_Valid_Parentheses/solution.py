class Solution:
    def isValid(self, s):
        dp = {"(":0,"[":1,"{":2}
        dm ={")":0,"]":1,"}":2}
        stack = []
        for ch in s:
            if ch in dp:
                stack.append(ch)
            else:
                if len(stack)>0 and dp[stack[-1]]==dm[ch]:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True