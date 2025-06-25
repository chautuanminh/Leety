
def main() :
    shit = [2, 5, 88, 7]
    hehe = 12
    for i in range(0,4):
        for j in range (0,4):
            #so can not repeat the number?
            #how should i exclude 
            if(i != j):
                sum = shit[i] + shit[j]
            else:
                continue
            if (sum == hehe):
                print("the position is {i} and {j}")
main()