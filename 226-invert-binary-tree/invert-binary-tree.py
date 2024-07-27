# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        while q:
            qsize = len(q)
            for _ in range(qsize):
                currNode = q.popleft()
                currNode.left, currNode.right = currNode.right, currNode.left
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

        return root



            

