package removeDuplicates

// Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	index := 0
	count := 1
	for i := 1; i < len(nums); {
		if nums[index] == nums[i] {
			if count < 2 {
				index++
				nums[index] = nums[i]
				count++
			}
		} else {
			index++
			nums[index] = nums[i]
			count = 1
		}
		i++
	}
	return index + 1
}
