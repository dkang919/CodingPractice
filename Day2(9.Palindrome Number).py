class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ = str(x)
        size = len(x_)
        
        L = []

        for i in range(size//2):
            if x_[i] != x_[-(i+1)]:
                return False

        return True




# improvements given by other challenger's insight

# 1. can reduce computational cost by doing initial check such as negative number cannot be palindrome

# 2. great approach of getting last digit number by using modulo expression to compare the first/second half digits 