# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            leftMax = max(leftSum, 0)
            rightMax = max(rightSum, 0)
            self.result = max(leftMax + rightMax + root.val, self.result)
            return max(root.val + leftMax, root.val + rightMax)
        dfs(root)
        return self.result
        