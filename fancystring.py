class Solution:
    def makeFancyString(self, s: str) -> str:

        #when count > 2 replace the rest with ""
        result = s[0]        # Start with first character
        count = 1
        for i in range (0, len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else: count = 1
            if count > 2:
                result += ""
            result += s[i]
            return result