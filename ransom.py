from typing import *
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1
        for z in ransomNote:
            if z not in counter:
                return False
            else: 
                counter[z] -= 1
                if counter[z] == 0:
                    counter.pop(z)
        return True                
def main():
    sol = Solution()
    ran = "hell"
    maga = "hello"
    result = sol.canConstruct(ran, maga)
    print(result)
main()