class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1],[1,1]]

        else:
            prev = []
            ans = []
            for i in range(numRows):
                if i == 0:
                    ans.append([1])
                    prev = [1]
                elif i == 1:
                    ans.append([1,1])
                    prev = [1,1]

                else:
                    L = [1]
                    for j in range(len(prev)-1):
                        L.append(prev[j]+prev[j+1])
                    L += [1]
                    ans.append(L)
                    prev = L[:]

        return ans


#### Best Runtime Solution

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            last_row = res[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(last_row[j] + last_row[j-1])

            new_row.append(1)

            res.append(new_row)

        return res



#### Best Memory Solution

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = pascal[i-1][j] + pascal[i-1][j-1]
            pascal.append(row)
        return pascal