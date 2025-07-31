from collections import *
from typing import *
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        nums.sort()
        total = nums[-1]
        for i in range (0, n-1):
            x = total 
            j = n - i - 2
            d[nums[j]] += 1
            if d[nums[j]] > 1:
                continue
            else:
                total += nums[j]
                if total < x:
                    return x
                else: continue
        return total              
def main():
    sol = Solution()
    nums =[1,1,0,1,1]
    result = sol.maxSum(nums)
    print(result)
main()
    