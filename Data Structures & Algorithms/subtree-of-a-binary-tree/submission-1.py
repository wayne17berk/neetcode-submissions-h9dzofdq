# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, p: Optional[TreeNode], subp: Optional[TreeNode]) -> bool:
        if not subp:
            return True
        if not p: 
            return False
        if  self.SameTree(p, subp):
            return True
        return (self.isSubtree(p.left, subp) or self.isSubtree(p.right, subp))
    def SameTree(self, p:Optional[TreeNode], subp:Optional[TreeNode])->bool:
        if not p and not subp:
            return True
        if p and subp and p.val == subp.val:
            return self.SameTree(p.left, subp.left) and self.SameTree(p.right, subp.right)
        return False
        

        