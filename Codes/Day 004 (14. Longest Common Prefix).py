class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = strs[0]

        size = len(strs[0])
        count = 0
        bucket = ""



        for i in range(1,len(strs)):
            if "" == strs[i]:
                return ""
            for j in range(len(strs[i])):
                if j < len(lcp):
                    #print(strs[i][j], lcp[j])
                    if strs[i][j] == lcp[j]:
                        
                        bucket += lcp[j]
                        #print(1, bucket)
                    else:
                        lcp = bucket[:]
                        bucket = ""
                        #print(2, lcp)
                else:
                    #print(3)
                    break
            #print(4, lcp, bucket)
            if (len(bucket) < len(lcp) )and (bucket !=""):
                lcp = bucket[:]
            bucket = ""

        return lcp
