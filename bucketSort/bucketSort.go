package main

import (
	"container/list"
	"fmt"
	"strconv"
)

func bucketSort(theArray []int, num int) {
	var theSort [99]int
	for i := 0; i < len(theArray); i++ {
		if theSort[theArray[i]] != 0 {
			theSort[theArray[i]]++
		} else {
			theSort[theArray[i]] = 1
		}
	}
	l := list.New()
	for j := 0; j < 99; j++ {
		if theSort[j] == 0 {
			fmt.Printf("_")
		} else {
			for k := 0; k < theSort[j]; k++ {
				fmt.Printf(strconv.Itoa(j) + " ")
				l.PushBack(j)
			}
		}
	}
	for e := l.Front(); e != nil; e = e.Next() {
		fmt.Print(e.Value)
	}
}
func main() {
	var theArray = []int{10, 1, 18, 30, 23, 12, 7, 5, 18, 17}
	fmt.Print("排序前")
	fmt.Println(theArray)
	fmt.Print("排序后")
	bucketSort(theArray, 11)
}
