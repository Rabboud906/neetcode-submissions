# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node, max_val_seen):
            if not node:
                return 0
            self.result += 1 if node.val >= max_val_seen else 0
            max_val_seen = max(max_val_seen,node.val)
            dfs(node.left,max_val_seen)
            dfs(node.right, max_val_seen)
            return self.result
        return dfs(root, root.val)


        