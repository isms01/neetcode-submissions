class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        # a and b slide forward, converging toward f(n-1) and f(n) at each step
        for _ in range(n - 1):
            a, b = b, a + b
        return b