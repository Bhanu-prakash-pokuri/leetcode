# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def search(root):
            nonlocal diameter
            if root is None:
                return 0
            lh=search(root.left)
            rh=search(root.right)
            diameter=max(diameter,lh+rh)
            return 1+max(lh,rh)
        search(root)
        return diameter