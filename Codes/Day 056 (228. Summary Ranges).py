class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = None
        end = None
        output = []

        if nums == []:
            return []

        for n in nums:
            if start is None:
                start = n
                end = n
            else:
                # case when in range
                if n - end == 1:
                    end = n
                # case when prev range overs
                else:
                    if start == end:
                        output.append(str(start))
                    else:
                        output.append(str(start)+"->"+str(end))
                    start = n
                    end = n

        if start not in output:
            if start == end:
                output.append(str(start))
            else:
                output.append(str(start)+"->"+str(end))

        return output




# replaceable

                    if start == end:
                        output.append(f"{start}")
                    else:
                        output.append(f"{start}->{end}")