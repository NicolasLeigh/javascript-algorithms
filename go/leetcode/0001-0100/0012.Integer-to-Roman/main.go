package main

import "fmt"

// Greedy
func intToRoman(num int) string {
	// 1000-M, 900-CM, 500-D, 400-CD, 100-C, 90-XC, 50-L, 40-XL, 10-X, 9-IX, 5-V, 4-IV, 1-I
	values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	res, i := "", 0
	for num != 0 {
		for values[i] > num {
			i++
		}
		num -= values[i]
		res += symbols[i]
	}
	return res
}

func main() {
	fmt.Println(intToRoman(1380))
}
