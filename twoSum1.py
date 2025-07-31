from collections import *
from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = defaultdict(int)
        x = 0
        for num in nums:
            counter[num] = x
            x += 1
            
        for i in range (0, len(nums)):
            rep = target - nums[i]
            if rep in counter and counter[rep] != i :# to find other than self --> sau nums[0] --> counter rep != 0?
                return[i, counter[rep]]
            else: continue
        return final
def main():
    nums = [3,3]
    target = 6
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
main()