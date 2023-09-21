class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        isPlus = 1
        size = len(digits)
        ans = [0]*size

        for i in range(size-1,-1,-1):
            if isPlus == 1:
                if digits[i] != 9:
                    ans[i] = digits[i]+1
                    isPlus = 0
                else:
                    ans[i] = 0
            else:
                ans[i] = digits[i]

        if isPlus == 1:
            ans = [1] + ans
            
        return ans


## The first solution is a much better process while the second one has better readability


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        sdigits = ""
        
        for n in digits:
            sdigits += str(n)

        sdigits = str(int(sdigits) + 1)

        return [int(a) for a in sdigits]