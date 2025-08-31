from collections import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        left, right = 0, 1
        d = defaultdict(int)
        count = 1
        temp = 0
        if s == "":
            return 0 
        d[s[0]] += 1
        if len(s) == 1:
            return 1
        while left < right and right < len(s):
            #add right, check hehe, if right in hehe --> increment left + remove s[left] until d[s[right]] == 1
            d[s[right]] += 1
            count += 1
            while d[s[right]] > 1:
                temp2 = s[left]
                count -= 1
                left += 1
                d[temp2] -= 1
            right += 1
            temp = max(count, temp)
        return temp
def main():
    sol = Solution()
    s = "abc abcbb"
    res = sol.lengthOfLongestSubstring(s)
    print(res)
main()