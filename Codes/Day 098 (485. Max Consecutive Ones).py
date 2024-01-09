class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        k = 0
        maxk = 0
        
        for n in nums:
            if n == 1:
                k += 1

            else:
                if k > maxk:
                    print(k)
                    maxk = k 
                    k = 0
                else:
                    k = 0

        if k > maxk:
            return k

        return maxk 