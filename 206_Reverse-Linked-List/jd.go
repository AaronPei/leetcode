package reverseList

type List struct {
	val  int
	next *List
}

func rervse(list *List) *List {
	var pre, cur *List
	pre, cur = nil, list
	for cur != nil {
		cur.next = pre
		pre = cur
		cur = cur.next
	}
	return pre
}

func main() {
	node1 := new(List)
	node1.val = 1
	node2 := new(List)
	node2.val = 2
	node3 := new(List)
	node3.val = 3
	node4 := new(List)
	node4.val = 4
	node1.next = node2
	node2.next = node3
	node3.next = node4
	rervse(node1)
}
