class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0 
        u = x

        while l <= u:
            mid = (l + u) // 2

            if mid**2 == x:
                return mid
            
            elif mid**2 < x:
                l = mid + 1

            else:
                u = mid - 1

        return l-1



# applied binary search algorithm
# achieved the best calculation speed with other 66% of the group
