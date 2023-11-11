
class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            num_  = 0
            for n in str(num):
                num_ += int(n)
            num = num_
            
        return num







## Best Runtime Solution

class Solution:
    def addDigits(self, num: int) -> int:
        nextNum = 0
        for n in str(num):
            nextNum += int(n)
        if 0 <= nextNum <= 9:
            return nextNum
        else:
            return self.addDigits(nextNum)