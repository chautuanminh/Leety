from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        # ouput [[1, 3]]
        # lastEnd [-1][1] => 3
        # start lastEnd
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = output[-1][1]
            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output
    
def main():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    results = sol.merge(intervals)
    print(results)

main()
