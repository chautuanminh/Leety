class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        verstappen = 0
        temp = nums[0]
        for num in nums: 
            d[num] += 1
            if d[num] > d[temp]:
                temp = num
        return temp
            