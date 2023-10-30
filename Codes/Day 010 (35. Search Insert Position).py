class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1

        while left <= right:
            
            mid = (left + right) // 2
            #print(left, right, mid, len(nums))
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1 

        return left



 # Binary Search