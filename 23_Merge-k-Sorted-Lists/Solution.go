/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package mergeTwoLists

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	var p = lists[0]
	length := len(lists)
	for i := 1; i < length; i++ {
		// 遍历List，合并List[0]与List[i]为List[0]
		p = mergeTwoLists(p, lists[i])
	}
	return p
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
