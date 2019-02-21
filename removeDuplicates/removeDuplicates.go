package removeDuplicates

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	index := 0
	for i := 1; i < len(nums); {
		if nums[index] != nums[i] {
			index++
			nums[index] = nums[i]
		}
		i++
	}
	return index + 1
}
