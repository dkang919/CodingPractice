# Efficient approach, and one of the top solutions are using hash table
# Credit to : kshatriyas
# We can iterate through the array once, and for each element, check if the 
# target minus the current element exists in the hash table. If it does, we have
# found a valid pair of numbers. If not, we add the current element to the hash table.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
	n = len(nums)
        
	for i in range(n):
	    complement = target - nums[i]
	    if complement in numMap:
		return [numMap[complement], i]
	    numMap[nums[i]] = i

	return [] # No solution found <- which will not happen by the question's pre-condition
