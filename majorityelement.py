class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        x = 0
        for num in nums:
            d[num] += 1
            x = num if d[num] > count else x
            count = max(d[num], count)
        return x
    