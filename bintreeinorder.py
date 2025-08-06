# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root: 
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
#### anoda one
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        pointer = root
        while pointer or stack:
            while pointer: 
                stack.append(pointer)
                pointer =  pointer.left
            #so now you need to start adding the elements from the top as you added 0 - n from the bottom--> latest left node 
            pointer = stack.pop()
            res.append(pointer.val)
            pointer = pointer.right
        return res