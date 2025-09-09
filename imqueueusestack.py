class MyQueue:

    def __init__(self):
        self.q1 = [] #always append
        self.q2 = [] #always pop
    def push(self, x: int) -> None:
        #basis --> stack --> append to the back 
        return self.q1.append(x)
    def pop(self) -> int:
        if not self.q2: 
            for i in range(len(self.q1)):
            #stacks will pop from the right(back of the queue) --> to get to the front
                a = self.q1.pop()
                self.q2.append(a)
        return self.q2.pop()
    def peek(self) -> int:
        if not self.q2: 
            while self.q1:
                self.q2.append(self.q1.pop()) 
        return self.q2[-1]
    def empty(self) -> bool:
        return max(len(self.q1), len (self.q2)) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()