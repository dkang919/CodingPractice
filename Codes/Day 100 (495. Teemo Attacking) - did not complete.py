class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res=0
        for i in range(len(timeSeries)-1):
            diff=timeSeries[i+1]-timeSeries[i]
            if diff<duration:
                res+=duration-diff
        return len(timeSeries)*duration-res
            

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        seconds = 0

        lastAttack = -1
        for i in range(len(timeSeries))[::-1]:
            if lastAttack < 0 or timeSeries[i] + duration <= lastAttack:
                seconds += duration
            else:
                seconds += lastAttack - timeSeries[i]
            
            lastAttack = timeSeries[i]

        return seconds

class Solution:
    def findPoisonedDuration(self, t: List[int], d: int) -> int:
        return d+sum(min(t[i+1]-t[i], d) for i in range(len(t)-1))