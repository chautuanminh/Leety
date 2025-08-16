#1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxy(root):# calculates the max depth of one tree
            if not root:
                return 0
            return 1 + max(maxy(root.left), maxy(root.right)) #already checks left and right for the current node

        if not root:
            return True
        if abs(maxy(root.left) - maxy(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
#2
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #just count the depth on both sides and compare
        #at any given moment check left and right of a root node compare the max depth\
        hehe = []
        temp = root
        def maxy(root):
            if not root:
                return 0
            return 1 + max(maxy(root.left), maxy(root.right))
        #now iterater for each node
        while hehe or temp:
            while temp:
                hehe.append(temp)
                temp = temp.left
            temp = hehe.pop()
            if abs(maxy(temp.left) - maxy(temp.right)) > 1:
                    return False
            temp = temp.right
        return True
