# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float("-inf")
        def s(node):
            nonlocal ans
            if node is None:
                return 0
            l=0
            r=0
            l=max(l,s(node.left))
            r=max(r,s(node.right))

            curr=node.val+l+r
            ans=max(ans,curr)
            return node.val+max(l,r)
        s(root)
        return ans

            
        