class Solution:
    def isMatch(self, s, p):        
        def calc_val(possible, i, j):
            if possible[i][j]!=-1:
                return possible[i][j]
            
            if j>=len(p):
                if i>=len(s):
                    return 1
                else:
                    return 0
                
            flag = 1 if (i<len(s)) and (p[j] in[s[i],"."]) else 0
    
            if j+1< len(p) and p[j+1]=="*":
                if calc_val(possible,i,j+2)==1:
                    possible[i][j] = 1
                elif flag==1:
                    possible[i][j] = calc_val(possible, i+1,j)
                else:
                    possible[i][j] = 0
                    
            else:
                if flag==0:
                    possible[i][j] = 0
                else:
                    possible[i][j] = calc_val(possible,i+1,j+1)    
            return possible[i][j]
        
        possible = [[-1]*(len(p)+1) for _ in range(len(s)+1)]
        
        return calc_val(possible, 0, 0)==1