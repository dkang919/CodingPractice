class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        L = [n for n in range(1,n+1)]

        for i in range(n):
            if (L[i] % 3 == 0) and (L[i] % 5 == 0):
                L[i] = "FizzBuzz"

            elif (L[i] % 3) == 0:
                L[i] = "Fizz"
        
            elif (L[i] % 5) == 0:
                L[i] = "Buzz"

            else:
                L[i] = str(L[i])

        return L


----------------------

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        toRet = []
        for i in range(1, n+1):
            if(i % 3 == 0 and i % 5 == 0): 
                toRet.append('FizzBuzz')
            elif(i % 3 == 0):
               toRet.append('Fizz')
            elif(i % 5 == 0):
                toRet.append('Buzz')
            else:
                toRet.append(str(i))
        
        return toRet