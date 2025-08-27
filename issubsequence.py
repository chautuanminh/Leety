class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tem = 0
        count = 0
        for i in range(len(t)):
            if tem >= len(s):
                break
            if s[tem] == t[i]:
                tem += 1
                count += 1
            else: continue
        if count == len(s):
            return True
        else: return False