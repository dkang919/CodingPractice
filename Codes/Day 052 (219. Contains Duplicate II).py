class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}
        if len(nums) < 2:
            return False

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]

            else:
                dic[nums[i]].append(i)

        for n in dic.keys():

            if len(dic[n]) == 0:
                pass
            else:
                for j in range(len(dic[n])-1):
                    for w in range(j+1,len(dic[n])):
                        if abs(dic[n][j] - dic[n][w]) <= k:
                            return True
        
        return False



### need more work...

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):
            return False
        for i in range(len(nums)):
            if len(nums[i:i+1+k])!=len(set(nums[i:i+1+k])):
                return True
        return False