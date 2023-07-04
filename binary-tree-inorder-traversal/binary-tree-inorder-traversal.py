# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Pre-order
#In order-> if left child is checked then check the node 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            output.append(root.val)
            traverse(root.right)
            return output

        return traverse(root)
        
