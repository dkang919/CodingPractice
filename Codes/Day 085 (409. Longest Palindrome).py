class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        lp = 0
        cleaned = sorted(Counter(s).values(), reverse=True)
        switch = 0

        for v in cleaned:
            if v % 2 == 0:
                lp += v
            else:
                if switch == 1:
                    if v-1 > 0:
                        lp += v-1
                else:
                    lp += v
                    switch = 1

        return lp