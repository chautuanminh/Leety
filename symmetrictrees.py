from collections import *
from typing import *

#official solution
# Definition for a binary tree node.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right: 
                return True
            if not left or not right:
                return False
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return dfs(root.left, root.right)
#not finished solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        le = []
        ri = []
        lef = root.left
        righ = root.right
        while lef or righ: 
            while lef or righ:
                if lef is None or righ is None:
                    return False
                if lef.val == righ.val:
                    le.append(lef)
                    ri.append(righ)
                    lef = lef.left
                    righ = righ.right
                else:
                    return False
            #pop the first element of ri and le
            #now the lef and righ points to null so assign back to the last element
            if lef.val != righ.val : 
                return False
            lef = le.pop()
            righ = ri.pop()
            lef = lef.right
            righ = righ.left
        return True

def main():
    null = None
    s = Solution()
    t = [1,2,2,3,null,4,3]
    tree = build_tree(t)  # Convert list to TreeNode
    res = s.isSymmetric(tree)
    print(res)
main()
