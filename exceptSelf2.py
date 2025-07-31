from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1 , 1
        rr = [0]* len(nums)
        ll = [0]* len(nums)
        ll[0] = l
        rr[-1] = 1
        for i in range (1, len(nums)):
            j = -i - 1
            l *= nums[i]
            r *= nums[j]
            rr[j] = r
            ll[i] = l
        return [l*r for l, r in zip(rr, ll)]
def main():
    nums = [1,2,3,4]
    sol = Solution()
    results = sol.productExceptSelf(nums)
    
main()