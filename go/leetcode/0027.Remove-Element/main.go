package main

func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[i], nums[j] = nums[j], nums[i]
			j++
		}
	}
	return j
}
