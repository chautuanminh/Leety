class Solution:
    def countBits(self, n: int) -> List[int]:
        #n + 1 loop
        #count "1"s for each i --> bin(n - 1)
        x = [0] * (n+1)
        for i in range (0, n+1):
            temp = i
            count = 0
            if temp == 0:
                x[temp] = 0
            while i > 0:
                if i % 2 == 1:
                    count += 1
                i //= 2
            x[temp] = count
        return x