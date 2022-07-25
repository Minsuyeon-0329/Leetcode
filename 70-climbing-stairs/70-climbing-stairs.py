import math

class Solution:
    def climbStairs(self, n: int) -> int:
        m = n // 2 + 1
        res = 0
        for i in range(m):
            res += int(math.factorial(i + (n-i*2)) / (math.factorial(i) * math.factorial(n-i*2)))
        return res