package main

import (
	"fmt"
	"math"
)

func firstMissingPositive(nums []int) int {
	n := len(nums)
	nums = buketSort(nums)
	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return n + 1
}
func buketSort(nums []int) []int {
	n := len(nums)
	for i := 0; i < n; i++ {
		fmt.Println(i)
		fmt.Println(nums)
		for nums[i] != i+1 {
			if nums[i] <= 0 || nums[i] > n || nums[i] == nums[nums[i]-1] {
				break
			}
			nums = swap(nums, i, nums[i]-1)
			fmt.Println(nums)
		}
	}
	return nums
}
func swap(nums []int, i, j int) []int {
	tmp := nums[i]
	nums[i] = nums[j]
	nums[j] = tmp
	return nums
}

func main() {
	nums := []int{3, 4, -1, 1}
	// nums := []int{-5, 1000}
	// fmt.Println(nums[10])
	fmt.Println(firstMissingPositive(nums))
	fmt.Println(math.MaxInt32)
}
