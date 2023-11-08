import numpy as np

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        for i in range(32):
            if (2**i) > n:
                break

            elif (2**i) == n:
                return True

        return False



### Best Runtime Answer
### Awesome idea


class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0 :
        return False
    if n == 1 :
        return True
    if n % 2 > 0:
        return False
    return self.isPowerOfTwo(n//2)