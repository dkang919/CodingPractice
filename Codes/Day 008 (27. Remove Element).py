class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

# got same intuition from the previous in-place algorithm 
# replaced condition and logic was same!