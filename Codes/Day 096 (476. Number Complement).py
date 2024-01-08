class Solution:
    def findComplement(self, num: int) -> int:
        
        bnum = bin(num)[2:]
        cnum = ""

        for c in bnum:
            if c == "0":
                cnum += "1"
            else:
                cnum += "0"

        return int(cnum,2)