from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #smallest range of 0 or 1 never 2
        #how can I be less lonely on this path
        #2 pointer jumping at different speed
        #a += 2 and b +=1
        #if a step = x + 2 and b step = b + 1 -> step
        #else not match then return listp[0] range list[0]
        i = 0
        ans = []
        while i < len(nums) :
            start = nums[i] 
            while i < len(nums)-i and nums[i+1] == nums[i] + 1:
              i += 1
            if start != nums[i]:
              ans.append(str(start) + "->" + str(nums[i])) 
            else:
                ans.append(str(nums[i]))
            i += 1
        return ans
def main() :
    nums = [0,1,2,77,78,79,80,82,82,83,83,84,85]
    nums.sort()
    sol = Solution()
    result = sol.summaryRanges(nums)
    print(result)
main()