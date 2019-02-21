/**
 * Definition for singly-linked list.
 */
package swapParis

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	var a, b *ListNode
	pre := &ListNode{0, head}
	head = head.Next
	for pre.Next != nil && pre.Next.Next != nil {
		a = pre.Next
		b = a.Next
		pre.Next, b.Next, a.Next = b, a, b.Next
		pre = a
	}
	return head
}
