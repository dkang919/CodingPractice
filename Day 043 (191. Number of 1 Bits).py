class Solution:
    def hammingWeight(self, n: int) -> int:

        ans = "{0:b}".format(n)

        #ans = bin(n)[2:]  
        #ans = ans.replace("0","") 

        ans = ans.replace("0","")

        return len(ans)
        



### Best Runtime solution 

## bit n & 1 masks bit
## add if above condition met
## shift n to calculate next bit position

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
          bit = n & 1 # bit mask
          ans += bit
          n >>= 1
        return ans