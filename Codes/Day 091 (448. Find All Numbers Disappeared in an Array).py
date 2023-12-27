class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        n = set(nums)
        L = []

        for i in range(1,length+1):
            if i not in n:
                L.append(i)

        return L


---------------------- best solution ------------------------------------


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)

        presence = [0] * n

        for e in nums:
            presence[e-1] = 1
        
        res = []
        for i in range(n):
            if not presence[i]:
                res.append(i +1)
        
        return res