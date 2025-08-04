from typing import *
from collections import *
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        left = 0
        right = 0
        maxy = 0
        #add the first 2
        # add another, if len(seen) > 2, remove left
        #count += 1 each time right traverse\
        #count -= 1 each time left increment
        for right in range (len(fruits)):
            d[fruits[right]] += 1

            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    d.pop(fruits[left])
                left += 1
            maxy = max(maxy, right - left + 1)
            right += 1 #only count when sucessful 
        return maxy

def main(): 
    sol = Solution()
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    res = sol.totalFruit(fruits)
    print(res)
main()