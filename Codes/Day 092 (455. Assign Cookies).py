class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g_ = sorted(g, reverse = True)
        s_ = sorted(s, reverse = True)

        count = 0
        size = len(s_)

        for i in range(len(g_)):
            if count >= size:
                break

            elif g_[i] <= s_[count]:
                count += 1

        return count