package firstMissingPositive

import "math"

func firstMissingPositive(nums []int) int {
	// 遍历数组，分别读取index值和vlaue
	for i, v := range nums {
		// 如果符合v=nums[v-1]或者v等于一个定数继续
		if i == v-1 || v == math.MaxInt32 {
			continue
		}
		// 显然不符合上述规则，i的位置上定义为一个常数
		nums[i] = math.MaxInt32
		for {
			// 重新计算v值应该在的位置，
			i = v - 1
			// 判断是否符合规则，符合则跳出循环
			if i < 0 || i >= len(nums) || nums[i] == v {
				break
			}
			// 交换位置，重新判断交换完位置的值
			nextV := nums[i]
			nums[i] = v
			v = nextV
		}
	}
	for i, v := range nums {
		if v == math.MaxInt32 {
			return i + 1
		}
	}
	return len(nums) + 1
}
