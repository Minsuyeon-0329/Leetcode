class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_d={}
        for stone in stones:
            s=stones_d.get(stone)
            if s is None:
                stones_d[stone]=1
                continue
            stones_d[stone] += 1
        j=0
        for jewel in jewels:
            if jewel not in stones_d:
                j+=0
            else:
                if stones_d[jewel]:
                    j+=stones_d[jewel]
        return j