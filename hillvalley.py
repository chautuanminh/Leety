from typing import *
class Solution:
  
    def countHillValley(self, nums: List[int]) -> int:
        hill = 0
        prev = 0
        after = 0
        new = [nums[0]]
        i = 0
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                new.append(nums[i+1])
                
        print(new)
        for i in range(1, len(new)-1):
            prev = i - 1
            after = i + 1
            if new[prev] > new[i] and new[after] > new[i]:
                hill += 1
            elif new[prev] < new[i] and new[after] < new[i]:
                hill += 1

        return hill
def main() :
    nums = [2,4,1,1,6,5]
    sol = Solution()
    result = sol.countHillValley(nums)
    print(result)
main()