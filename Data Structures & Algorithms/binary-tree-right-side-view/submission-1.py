# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if not root:
            return res
        q.append(root)
        while len(q)>0:
            rightModeNode = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightModeNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightModeNode:
                res.append(rightModeNode.val)
        return res