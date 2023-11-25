class Solution:
    def reverseVowels(self, s: str) -> str:
        
        d = [let for let in s]
        k = []
        for _ in range(len(s)):
            if s[_].lower() in {"a","e","i","o","u"}:
                d[_] = "_"
                k = [s[_]] + k

        i = 0
        for j in range(len(d)):
            if d[j] == "_":
                d[j] = k[i]
                i += 1

        ans = ""
        for v in d:
            ans += v

        return ans