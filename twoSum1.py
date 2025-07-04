from collections import *
from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = defaultdict(int)
        #how to not use double loop to figure this out?
        #you still have to try all combination
        #even if you go with find the constructing elements you still need double for loop
        for i in range (0, target + 1):
            x = target  - i
            counter[x] = i
        for t in nums:
            if t in counter and counter[t] in nums:
                return True
            else:
                continue
        return False
def main():
    nums = [0,1,2,3,4,5]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
main()