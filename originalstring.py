from itertools import groupby
class Solution:
    def possibleStringCount(self, word: str) -> int:
        #find possible combination: take a count var, decrease until 1
        #use itertools.groupby 
        grouped = [(k, len(list(group))) for k, group in groupby(word)]
        total = 1
        x = 0
        for k, count in grouped:
            if count == 1:
                continue #no count for one letter start at 1 since 
            else: 
                #example count = 4 --> 3
                #for each k return total += count - 1
                total += (count -1)
        return total