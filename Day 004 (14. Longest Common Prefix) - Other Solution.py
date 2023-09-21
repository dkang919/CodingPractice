class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = ""

        strs=sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):
	    if(first[i] != last[i]):
		return lcp
	    lcp+=first[i]

        return lcp



# key takeaway

# use sorted to re-line the list in order 

# then you can compare the first and the last without going through all lists

# then the least ranged by min can let do the comparison for the common prefixes!
