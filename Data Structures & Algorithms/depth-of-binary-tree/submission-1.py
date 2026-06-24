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
        st = deque([root])        
        while st:
            for _ in range(len(st)):
                node = st.popleft()
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            maxD+=1
        return maxD