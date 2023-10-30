## Best Answer
## RUNTIME 132ms (0.0047)
## Memory 17.8MB (0.17)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        L = sorted(nums)

        return L[len(nums)//2]


## sort function seems like to use less memory as it sorts within the array/list
## but sorted creates new sequence, which consumes less memory as the L size increases




### Best Memory use (99.88%)  ~ (0.0012)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidates = set(nums)

        for n in candidates:
            c = 0
            for i in range(len(nums)):
                if int(n) == nums[i]:
                    c += 1
                if c >= len(nums)/2:
                    return n