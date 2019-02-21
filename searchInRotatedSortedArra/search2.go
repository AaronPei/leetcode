package searchInRotatedSortedArra

/**
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
*/
func search2(nums []int, target int) bool {
	first := 0
	last := len(nums)
	for first != last {
		mid := (first + last) / 2
		if target == nums[mid] {
			return true
		}
		if nums[first] < nums[mid] {
			if nums[first] <= target && target < nums[mid] {
				last = mid
			} else {
				first = mid + 1
			}
		} else if nums[first] > nums[mid] {
			if nums[mid] < target && target <= nums[last-1] {
				first = mid + 1
			} else {
				last = mid
			}
		} else {
			first++
		}
	}
	return false
}
