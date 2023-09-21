class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        isWord = 0
        c = 0

        for i in range(len(s)-1,-1,-1):
            if isWord == 1 and s[i] != " ":
                c += 1
            elif isWord == 0 and s[i] != " ":
                c += 1
                isWord = 1
            elif isWord == 1 and s[i] == " ":
                return c

        return c



## The first solution improved its processing performance as it travels from the back of the string
## so that it can offer to stop the calculation as soon as it receives the length of the last word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.split()[-1])