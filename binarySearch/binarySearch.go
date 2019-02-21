package main

import (
	"fmt"
)

// 在已经排好序的数组中查找
// 递归
func binarySearch(array []int, start, end, key int) int {
	mid := (end-start)/2 + start
	if key == array[mid] {
		return mid
	} else if key < array[mid] {
		return binarySearch(array, start, mid-1, key)
	} else if key > array[mid] {
		return binarySearch(array, mid+1, end, key)
	}
	return -1
}

func binarySearch1(array []int, start, end, key int) int {
	// 只有start 小于等于 end的时候继续循环
	for start <= end {
		mid := (end-start)/2 + start
		if key < array[mid] {
			end = mid - 1
		} else if key > array[mid] {
			start = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

func main() {
	array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	key := 4
	fmt.Println(binarySearch(array, 0, 8, key))
	fmt.Println(binarySearch1(array, 0, 8, key))
}
