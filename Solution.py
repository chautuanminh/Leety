class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s)-1
        while l < r :
            if (s[l] != s[r]) :
                return False
            else:
                continue
            #increment the pointer for the string
            l+=1
            r-=1

        return True
def main():
    s = "123"
    sol = Solution()
    result = sol.isPalindrome(s)
    print({result})
main()
