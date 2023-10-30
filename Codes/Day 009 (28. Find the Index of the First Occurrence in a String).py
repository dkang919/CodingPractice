class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == needle:
            return 0

        L = []
        size = len(needle)

        for _ in range(len(haystack)):
            if haystack[_] == needle[0]:
                if (_ + size) <= len(haystack):
                    L.append(_)

        for i in L:
            if haystack[i:i+size] == needle:
                return i

        return -1


# above one is better !
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1

        else:
            L = []
            size = len(needle)

            for _ in range(len(haystack)):
                if haystack[_] == needle[0]:
                    if (_ + size) <= len(haystack):
                        L.append(_)

            if len(L) == 0:
                return 0

            for i in L:
                if haystack[i:i+size] == needle:
                    return i

'''
