/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    return dfs(root, nil, nil)
}

func dfs (root *TreeNode, low, high *int) bool{
    if root == nil {
        return true
    }
    if low!=nil && root.Val <= *low {
        return false
    }
    if high!=nil && root.Val >= *high {
        return false
    }
    //left child
    //when we search the left, we expect that the left child is not greater than the current node
    // or in other words, leftChild <currentNode. We need to make sure the leftChild is less than the current node, but also 
    //if the left node is on a right subtree, it is not smaller than it's parent.

    //when we search the right, we expect that the right child is not less than the current node
    return dfs(root.Left, low, &root.Val) && dfs(root.Right, &root.Val, high)
}