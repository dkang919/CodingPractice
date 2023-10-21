class Solution:
    def reverseBits(self, n: int) -> int:

        n_ = "{0:b}".format(n)

        n_ = n_[::-1]

        while len(n_) < 32:
            n_ += "0"

        return int(n_,2)
    
    
### New Learning

# & is a  bitwise operator used to perform a bitwise AND opration
# Simply, bit-logic AND operator

# >> << is used to shift bit by spaces 
# ex. 2 << 5 shift binary 2 by 5 bits -> 0b10 -> 0b1000000

# ^= is augmented assignment operator
# need more study on use 
