package main

import (
	"fmt"
)

func findMin(nums []int) int {
	low, high := 0, len(nums)-1

	for low < high {
		mid := low + (high-low)/2
		if nums[mid] > nums[high] {
			// If nums[mid]>nums[high], the right range isn't sorted, min should be always in [mid+1, high], so low=mid+1
			low = mid + 1
		} else if nums[mid] < nums[low] {
			// If nums[mid]<nums[low], the left range isn't sorted, min should be always in [low+1, mid], so high=mid and low=low+1
			high = mid
			low++
		} else {
			// Else nums[low] <= nums[mid] <= nums[high], let high=high-1.
			// Be careful, in this case, the min not necessarily be nums[low], because the elements in the nums array are not unique. 
			// Take [2,1,2,2,2] for example, the min isn't the nums[low], so we need to let high=high-1 to shrink the range.
			high--
		}
	}

	return nums[low]
}

func main() {
	nums := []int{3, 4, 5, 1, 2}
	fmt.Println(findMin(nums)) // Output: 1
}
