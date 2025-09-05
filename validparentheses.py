class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        cc = []
        for c in s:
            #if c is open parentheses
            if c not in pairs: 
                cc.append(c)
            else:
                #if parentheses is closing --> find if the fist element of the stack (open paren)
                #hashmap check
                if cc and pairs[c] == cc[-1]:
                    cc.pop()
                else: return False
        return False if cc else True