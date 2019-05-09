class Solution:
                              
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start = ord("a")
        
        letters_dict = [[]] * 26
            
        for word in wordDict:
            letters_dict[ord(word[0]) - start].append(word)
            
        mask = [0] * (len(s) + 1)
        mask[0] = 1
        
        for i in range(len(s)):
            if mask[i] == 1:
                for w in letters_dict[ord(s[i]) - start]:
                    if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                        mask[i + len(w)] = 1
                        
        return mask[len(s)] == 1
        