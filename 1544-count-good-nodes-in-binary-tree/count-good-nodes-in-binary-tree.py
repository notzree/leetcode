# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # basically checking if a node has the maxValue in it's path to the root
        self.goodNodes = 0 # The root is always good
        # Traverse dfs until the bottom of the tree
        def dfs(root, maxValue):
            global goodNodes
            if root is None:
                return 
            maxValue = max(root.val, maxValue)
            if root.val == maxValue:
               self.goodNodes+=1
            dfs(root.right, maxValue)
            dfs(root.left,maxValue)
        dfs(root, root.val)
        return self.goodNodes



        