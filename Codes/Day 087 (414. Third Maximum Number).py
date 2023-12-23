class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        L = sorted(set(nums))

        if len(L) == 2:
            return L[-1]

        elif len(L) == 1:
            return L[0]

        return L[-3] 


---------------------------------------------------------

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numbers = list(set(nums))
        if len(numbers) <= 2:
            return max(numbers)
        numbers.sort(reverse=True)
        return numbers[2]