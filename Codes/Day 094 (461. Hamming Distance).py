class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_ = bin(x)[2:]
        y_ = bin(y)[2:]
        diff = len(x_) - len(y_)

        if diff < 0:
            x_ = '0'*abs(diff) + x_
        elif diff > 0:
            y_ = ('0'*diff) + y_

        count = 0

        for i in range(len(x_)):
            if x_[i] != y_[i]:
                count += 1

        return count

---------------------------------------------------------------------------

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        sum = 0
        for i in range(32):
            if a & 1 == 1:
                sum += 1
            a >>= 1
        return sum