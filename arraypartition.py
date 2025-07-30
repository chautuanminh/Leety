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
        