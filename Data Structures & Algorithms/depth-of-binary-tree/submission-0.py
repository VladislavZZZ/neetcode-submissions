# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD=0
        if not root:
            return maxD
        st = [(root,1)]        
        while st:
            node, d = st.pop()
            maxD = max(maxD, d)
            if node.left:
                st.append((node.left, d+1))
            if node.right:
                st.append((node.right, d+1))
        return maxD