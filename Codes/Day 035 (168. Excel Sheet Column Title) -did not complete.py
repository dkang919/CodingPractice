# Solution by vanAmsen

# bit of modification from my end

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        ans = ""

        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            ans = (chr(65 + remainder)) + ans
            #print(columnNumber,ans) 

        return ans



## This approach is interesting, while = 0 makes it stop, where it will eventually happen
## divmod is super helpful to get quotient as well as the remainder
## col number is reduced by 1 for every interation as it moves up