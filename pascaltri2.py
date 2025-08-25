class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final = [[1]]  # start with first row
        
        for i in range(1, rowIndex + 1):
            prev = final[-1]
            # pad with zeros at both ends
            subs = [0] + prev + [0]
            yuh = []
            # build the new row by adding neighbors
            for k in range(len(subs) - 1):
                yuh.append(subs[k] + subs[k+1])
            final.append(yuh)
        
        return final[-1]
