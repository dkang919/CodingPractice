class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s = sorted(s)
        t = sorted(t)
        count = 0
        size = len(s)

        while count < size:
            if s[count] != t[count]:
                return t[count]

            count += 1
            
        return t[-1]


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        return list((Counter(t) - Counter(s)).keys())[0]