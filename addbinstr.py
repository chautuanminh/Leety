class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = len(a)
        y = len(b)
        carry = 0
        i = 0
        final = ""
        j = x - i - 1
        k = y - i - 1
        while j in range (0, x) or k in range (0, y) or carry:
            #if a[j] or b[j] exists else 0
            
            if j in range (0, x):
                p = int(a[j])
            else: p = 0
            if k in range (0, y):
                o = int(b[k])
            else: o = 0
            summy = p + o + carry 
            carry = summy // 2
            digit = summy % 2
            hehe = str(digit)
            #concatenate in reverse
            final = final + hehe
            i += 1
            j = x - i - 1
            k = y - i - 1
        return final[::-1]