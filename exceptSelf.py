#exceptSelf
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final = []
        for i in range (0, len(nums)):
            cum = 1
            count = 0
            while (count < len(nums)):
                if (count != i):
                    cum *= nums[count]
                    count += 1 
                else:
                    count += 1
                    continue
            final.append(cum)
        return final
        

def main():
    nums = [1,2,3,4]
    sol = Solution()
    results = sol.productExceptSelf(nums)
    print(results)
    
main()