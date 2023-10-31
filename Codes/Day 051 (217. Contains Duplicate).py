class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        h = set()

        for n in nums:
            if n in h:
                return True
            h.add(n)

        return False
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(set(nums)) != len(nums) 


# Both my solutions, and general answers!