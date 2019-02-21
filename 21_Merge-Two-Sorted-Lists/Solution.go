package

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var head, tail *ListNode
	if l1 == nil && l2 == nil {
		return l1
	}
	if l1 != nil && l2 == nil {
		return l1
	}
	if l1 == nil && l2 != nil {
		return l2
	}
	if l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			head, tail, l1 = l1, l1, l1.Next
		} else {
			head, tail, l2 = l2, l2, l2.Next
		}
		for l1 != nil && l2 != nil {
			if l1.Val <= l2.Val {
				tail.Next, l1 = l1, l1.Next
			} else {
				tail.Next, l2 = l2, l2.Next
			}
			tail = tail.Next
		}
		if l1 != nil {
			tail.Next = l1
		}
		if l2 != nil {
			tail.Next = l2
		}
	}
	return head
}
