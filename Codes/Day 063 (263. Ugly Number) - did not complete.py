## Solutions by abhinavsatish34 and md2030




class Solution:
    def isUgly(self, n: int) -> bool:
        return False if n<=0 else (2*3*5)**32 % n == 0


    def isUgly2(self, n: int) -> bool:
        if n<=0: return False
        while n%2==0: n/=2
        while n%3==0: n/=3
        while n%5==0: n/=5
        return n==1



    def isUgly3(self, n: int) -> bool:
        if n<=0: return False
        while n%3==0: n//=3
        while n%5==0: n//=5
        return ( n & (n-1) ) == 0


class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1