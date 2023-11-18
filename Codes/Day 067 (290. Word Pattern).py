class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False

        dic = {}

        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = ss[i]

            else:
                if dic[pattern[i]] != ss[i]:
                    return False

        return len(dic.keys()) == len(set(dic.values()))