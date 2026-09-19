# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        small = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    small.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        sorted_small = sorted(small)
        if k < 0 or k > len(sorted_small):
            return -1
        else:
            return sorted_small[k-1]

            