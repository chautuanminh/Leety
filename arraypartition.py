from collections import *
from typing import *
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #group similar values
        nums.sort()
        #how do i group them? 
        i = 0
        n = len(nums)
        count = 0
        while i < n - 1:
            count += min(nums[i], nums[i+1])
            i+=2
        return count
def main():
    sol = Solution()
    nums = [6,2,6,5,1,2]
    result = sol.arrayPairSum(nums)
    print(result)
main()