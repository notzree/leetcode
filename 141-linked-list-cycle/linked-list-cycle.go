/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    visited := make(map [*ListNode] struct{})
    for head != nil {
        if _, exists := visited[head]; exists {
            return true
        }
        visited[head] = struct{}{}
        head = head.Next
    }
    return false
}