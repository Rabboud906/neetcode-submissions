# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        cursor = root

        while cursor:
            if p.val > cursor.val and q.val > cursor.val:
                cursor = cursor.right
            elif p.val < cursor.val and q.val < cursor.val:
                cursor = cursor.left
            else:
                return cursor
        