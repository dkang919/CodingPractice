class Solution:
    def isPowerOfThree(self, n: int) -> bool:


        if n < 1:
            return False

        k = 0
        while 3**k < n:
            k += 1

        return (3**k) == n