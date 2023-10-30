class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]

        else:
            prev = [1]
            for i in range(rowIndex):

                L = [1]
                for j in range(len(prev)-1):
                    L.append(prev[j]+prev[j+1])
                prev = L + [1]

            return L + [1]