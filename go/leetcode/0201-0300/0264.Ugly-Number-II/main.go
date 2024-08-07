package main

import (
	"fmt"
)

func nthUglyNumber(n int) int {
	dp, p2, p3, p5 := make([]int, n+1), 1, 1, 1
	dp[0], dp[1] = 0, 1
	for i := 2; i <= n; i++ {
		x2, x3, x5 := dp[p2]*2, dp[p3]*3, dp[p5]*5
		dp[i] = min(x2, x3, x5)
		if dp[i] == x2 {
			p2++
		}
		if dp[i] == x3 {
			p3++
		}
		if dp[i] == x5 {
			p5++
		}
	}
	return dp[n]
}

func main() {
	n := 10
	result := nthUglyNumber(n)
	fmt.Println(result) // Output: 12
}
