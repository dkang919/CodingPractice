# my best answer 
# 59 ms / 16.9 mb 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = ""
        
        for l in s:
            if l.isalnum():
                s2 += l

        for i in range(len(s2)):
            if s2[i].lower() == s2[-i-1].lower():
                pass
            else:
                return False

        return True



## BEST RUNTIME

21 ms / 17.8 mb

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        
        return s == s[::-1]

