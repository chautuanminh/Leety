class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #this problem should be solved using sliding windows
        #to have a window of size "k" --> fixed size so when you move that 
        for i in range(0, len(blocks)-k+1):
            count = 0
            left = i
            right = i + k - 1 #this is correct
            for t in range (left, right+1):
                if blocks[t] == "W":
                    count += 1
            #so now i need something to get the value of count and compare prev values
            #so now count holds the number
            #compare count to it's previous self
            if i == 0:
                op = count
            else:
                op = min(op, count)
        return op