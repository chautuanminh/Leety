class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #so if the count of each is different then return false 
        ss = len(s)
        tt = len(t)
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        d3 = defaultdict(int)
        if ss != tt:
            return False
        for i in range(ss):
            if s[i] not in d3:
                d3[s[i]] = t[i]
            if d3[s[i]] != t[i]:
                return False
            d1[s[i]] += 1
            d2[t[i]] += 1
            if d1[s[i]] != d2[t[i]]:
                return False
        #one character mapped to another
        return True