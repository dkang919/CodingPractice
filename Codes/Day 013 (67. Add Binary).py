class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # does it make sense to match the length of both input str 
        # how about making new string space to fill in those values? 
        # which would be more important completeness vs ensuring performance

        ans = ""

        la = len(a)
        lb = len(b)
        
        if la > lb:
            diff = la-lb
            b = "0"*diff + b
        elif lb > la:
            diff = lb-la
            a = "0"*diff + a
    
        isPlus = 0
        for i in range(len(b)-1, -1, -1):
            num = isPlus + int(b[i]) + int(a[i])
            
            if num == 2:
                isPlus = 1
                ans = "0" + ans 

            elif num == 3:
                isPlus = 1
                ans = "1" + ans 

            else:
                ans = str(num) + ans
                if isPlus == 1:
                    isPlus = 0

        if isPlus == 1:
            return "1" + ans

        return ans



#######
# Best Answer 
# Used int method's second parameter int(a,2)   ~ basing 2 instead of default =base10 

# as the source code probably written in C, making the process much more intuitive and fast!

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=int(a,2)
        m=int(b,2)
        return str(bin(n+m))[2:]





