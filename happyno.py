class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def recur(x, n):
            if n == 0: 
                return x
            t = n % 10
            x += t * t
            return recur(x, n//10)
        while n not in seen: 
            if n == 1: 
                return True
            seen.add(n)
            n = recur(0, n)
        return False