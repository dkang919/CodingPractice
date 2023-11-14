# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        mid = n // 2
        lower = 1
        upper = n
        ans = upper

        while lower < upper:
            if isBadVersion(mid) == True:
                ans = mid
                upper = mid - 1
                if isBadVersion(upper) == True:
                    ans = upper
                    
            else:
                if isBadVersion(lower) == True:
                    return lower
                lower = mid + 1

            mid = ((upper - lower) // 2) + lower

        return ans


# best of the best solution
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left