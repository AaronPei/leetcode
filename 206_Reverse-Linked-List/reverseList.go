/**
 *Definition for singly-linked list.
 */
package reverseList

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prve, cur *ListNode
	prve, cur = nil, head
	for cur != nil {
		cur.Next, prve, cur = prve, cur, cur.Next
	}
	return prve
}
