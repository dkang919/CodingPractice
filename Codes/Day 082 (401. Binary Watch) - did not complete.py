class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for Hs in range(0, min(turnedOn, 4) + 1):
            Ms = turnedOn - Hs
            if not 0 <= Ms <= 6: continue
            hcomb = itertools.combinations(range(4), Hs)
            mcomb = itertools.combinations(range(6), Ms)
            hcomb = tuple(map(lambda hs: 0 + sum(2 ** i for i in hs), hcomb))
            mcomb = tuple(map(lambda ms: 0 + sum(2 ** i for i in ms), mcomb))
            res += ['{}:{:02d}'.format(h, m) for h in hcomb
                    for m in mcomb if h < 12 and m < 60]
        return res


HOURS = [8, 4, 2, 1]
MINUTES = [32, 16, 8, 4, 2, 1]
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for t in range(turnedOn+1):
            h_on = min(t, 4)
            m_on = turnedOn - h_on

            for hs in combinations(HOURS, h_on):
                for ms in combinations(MINUTES, m_on):
                    h_total = sum(hs)
                    if h_total > 11:
                        continue
                    m_total = sum(ms)
                    if m_total > 59:
                        continue
                    res.append(f'{h_total}:{m_total:02}')
        return res