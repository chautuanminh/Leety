from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #should there be two dictionaries?
        counter = defaultdict(int)
        for letter  in s:
            counter[letter] += 1
        for letterx in t:
            if letterx not in counter:
                return False
            else: 
                counter[letterx] -= 1
                if counter[letterx] == 0:
                    counter.pop(letterx)

        if not counter:
            return True
        else:
            return False
def main():
    s = "a"
    t = "ab"
    sol = Solution()
    result = sol.isAnagram(s, t)
    print(result)
main()