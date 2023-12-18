class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        count = 0

        if s == "":
            return True

        for item in t:
            if count == len(s):
                return True
            
            if s[count] == item:
                count += 1


        return count == len(s)
