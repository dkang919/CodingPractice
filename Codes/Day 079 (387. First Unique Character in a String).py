class Solution:
    def firstUniqChar(self, s: str) -> int:


        for i in range(len(s)-1):
            
            if s[i] == "_":
                pass

            elif s[i] in s[i+1:]:
                s = s.replace(s[i],"_")
            
            else:
                return i
        
        if len(s) == 1:
            return 0 

        for k in range(len(s)):
            if s[k] != "_":
                return k
                
        return -1