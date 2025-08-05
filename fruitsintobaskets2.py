class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
             #return n - i + 1
            count = 0
            n = len(baskets)
            for fruit in fruits: 
                unset = 1
                for i in range(n):
                    x = baskets[i]
                    if fruit <= x:
                        unset = 0
                        baskets[i] = 0
                        break
                count += unset
            return count