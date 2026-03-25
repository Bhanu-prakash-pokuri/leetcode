# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        l=[root.val]
        l+=self.preorderTraversal(root.left)
        l+=self.preorderTraversal(root.right)
        return l
        # if root==None:
        #     return []
        # s=[root]
        # r=[]
        # while s:
        #     n=s.pop()
        #     r.append(n.val)
        #     if n.right:
        #         s.append(n.right)
        #     if n.left:
        #         s.append(n.left)
        # return r

        