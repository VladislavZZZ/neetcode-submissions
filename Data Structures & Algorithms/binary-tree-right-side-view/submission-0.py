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
        cur_level =0
        q.append((root,cur_level+1))
        while len(q)>0:
            node, level = q.popleft()
            if level > cur_level:
                res.append(node.val)
                cur_level+=1
            if node.right:
                q.append((node.right,level+1))
            if node.left:
                q.append((node.left, level+1))
        return res