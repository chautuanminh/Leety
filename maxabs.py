class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        prev = 0
        for i in range (0, len(nums)-1):
            temp = abs(nums[i+1] - nums[i])
            prev = max(temp, prev)
        return max(prev, abs(nums[0]-nums[-1]))
            #should it be 0? since the smallest possible dif is 0 so it should be fair since we're picking out max