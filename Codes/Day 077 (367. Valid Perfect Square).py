class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        mid = (num // 2) + 2
        
        for i in range(mid):
            if i**2 == num:
                return True

            elif i**2 > num:
                return False

        return False

import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        return math.sqrt(num) == int(math.sqrt(num))


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if isinstance(num, int):
            sqrt_num = int(num ** 0.5)
            return sqrt_num * sqrt_num == num
        else:
            return False