package findMaxConsecutiveOnes

func findMaxConsecutiveOnes(nums []int) int {
	max := 0
	nowMax := 0
	for _, v := range nums {
		if v == 1 {
			nowMax++
		} else {
			if nowMax > max {
				max = nowMax
			}
			nowMax = 0
		}
	}
	if max > nowMax {
		return max
	}
	return nowMax
}
