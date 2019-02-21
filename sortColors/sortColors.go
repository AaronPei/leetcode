package main

// 输入: [2,0,2,1,1,0]
// 输出: [0,0,1,1,2,2]
import (
	"fmt"
)

// 由于只有0，1，2三种数字，所以用计数法排序。再赋值回去。
func sortColors(nums []int) {
	var count = [3]int{0, 0, 0}
	for i := 0; i < len(nums); i++ {
		count[nums[i]]++
	}
	fmt.Println(count)
	for i, index := 0, 0; i < len(count); i++ {
		for j := 0; j < count[i]; j++ {
			nums[index] = i
			index++
		}
	}
	fmt.Println(nums)
}

func main() {
	var nums = []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
}
