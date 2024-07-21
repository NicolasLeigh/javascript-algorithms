package main

import (
	"fmt"
)

func longestConsecutive(nums []int) int {
	numSet := make(map[int]bool)
	for _, num := range nums {
		numSet[num] = true
	}

	longest := 0
	for num := range numSet {
		if !numSet[num-1] {
			currentNum := num
			currentStreak := 1

			for numSet[currentNum+1] {
				currentNum++
				currentStreak++
			}

			if currentStreak > longest {
				longest = currentStreak
			}
		}
	}

	return longest
}

func main() {
	fmt.Println(longestConsecutive([]int{100, 4, 200, 1, 3, 2})) // Output: 4
}