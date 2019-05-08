from collections import deque

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        letters = set()
        
        for word in words:
            letters = letters.union(set(word))    
        next_l = {}
        prev = {}
        for l in letters:
            next_l[l] = []
            prev[l] = 0
        for w1, w2 in zip(words[:-1],words[1:]):
            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    next_l[l1].append(l2)
                    prev[l2] += 1
                    break
        q = deque()
        output = []
        for l in prev:
            if prev[l] == 0:
                q.append(l)
        while len(q) > 0:
            # for the smallest lexigraphical ordre possible
            q = deque(sorted(q)) 
            cur_l = q.popleft()
            output.append(cur_l)
            for n_l in next_l[cur_l]:
                prev[n_l] -= 1
                if prev[n_l] == 0:
                    q.append(n_l)
        if len(output) == len(letters):
            return "".join(output)
        else:
            return ""