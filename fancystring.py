class Solution:
    def makeFancyString(self, s: str) -> str:
        #when count > 2 replace the rest with ""
        result = s[0]        # Start with first character
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                result += s[i]

        return result
                    