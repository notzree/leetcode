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
    //When we go to the left, we keep our left boundary the same, but update thright boundary.
    // low < leftChild < currentNode

    //when we search the right, we expect that the right child is not less than the current node
    //currentNode < rightChild < high
    return dfs(root.Left, low, &root.Val) && dfs(root.Right, &root.Val, high)

    //example on [5,1,4,null,null,3,6]
    //When we go from 5->4, our range is: x > 5 (update low)
    //when we go from 4->3, our range is:  5<x<4 (update high) which is impossible
}