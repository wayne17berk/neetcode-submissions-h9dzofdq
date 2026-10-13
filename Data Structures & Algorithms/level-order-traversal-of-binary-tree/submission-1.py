# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res=[]
        # depth=0
        # def dfs(root, depth)
        #     if not root:
        #         return []
        #     if len(res)==depth:
        #         res.append([])
        #         res.append(root.val)
        #     else:
        #         depth+=1
        #         return dfs(root.left, depth ) and dfs(root.right, depth)
        # dfs(root, 0)
        # return res
        res = []

        def dfs(root, depth):
            if not root:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res