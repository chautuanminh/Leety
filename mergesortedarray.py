class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #add and then sort?
        for i in range (n):
            t = m + i
            nums1[t] = nums2[i]
        nums1.sort()
        return nums1