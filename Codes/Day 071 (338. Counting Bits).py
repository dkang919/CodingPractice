class Solution:
    def countBits(self, n: int) -> List[int]:
        
        L = []

        for i in range(n+1):
            j = bin(i)[2:]
            k = 0 
            for l in j:
                if l == "1":
                    k +=1

            L.append(k)

        return L