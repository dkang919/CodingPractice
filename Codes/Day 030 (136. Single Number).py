# my best answer 
# 121 ms / 18.8 mb 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        numBag = set(nums)

        total = 0
        for n in nums:
            total += n

        for item in numBag:
            total -= 2*item
     
        return -total

## best runtime 
## binary bit operator - amazing...

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x