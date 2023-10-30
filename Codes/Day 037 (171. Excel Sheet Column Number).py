class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        k = 0

        for letter in columnTitle[::-1]:
            ans += (ord(letter)-64)*(26**k)
            k += 1

        return ans