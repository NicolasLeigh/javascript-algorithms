package main

func isPowerOfThree(num int) bool {
	for num >= 3 {
		if num%3 == 0 {
			num = num / 3
		} else {
			return false
		}
	}
	return num == 1
}