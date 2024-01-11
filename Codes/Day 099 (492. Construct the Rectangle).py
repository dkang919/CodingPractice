class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        k = int(sqrt(area))

        if k**2 == area:
            return [k,k]

        while k > 1:
            if (area % k) == 0:
                break
            k -= 1

        
        if k != 1:
            j = area // k
            return [j,k]

        return [area,1]

        