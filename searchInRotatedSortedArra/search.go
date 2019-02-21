package searchInRotatedSortedArra

// Search in Rotated Sorted Array
/**
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

采用二分查找的方法，注意边界值的确定。
*/
func search(nums []int, target int) int {
	first := 0
	last := len(nums)
	for first != last {
		mid := (first + last) / 2
		if target == nums[mid] {
			return mid
		}
		// 因为有序数组经过旋转，确保一直先在有序的数组中寻找target，所以先对比first和mid，
		if nums[first] < nums[mid] {
			if nums[first] <= target && target < nums[mid] {
				last = mid
			} else {
				first = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[last-1] {
				first = mid + 1
			} else {
				last = mid
			}
		}
	}
	return -1
}
