package main

import "fmt"

// Please note the difference between 0062 and 0063
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m := len(obstacleGrid)
	n := len(obstacleGrid[0])

	// Initialize 2D dp array
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	// Base cases
	for i := 0; i < m && obstacleGrid[i][0] == 0; i++ {
		dp[i][0] = 1
	}
	for j := 0; j < n && obstacleGrid[0][j] == 0; j++ {
		dp[0][j] = 1
	}

	// Fill dp array
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if obstacleGrid[i][j] == 0 {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}

	return dp[m-1][n-1]
}

func main() {
	obstacleGrid := [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println("Number of unique paths with obstacles:", uniquePathsWithObstacles(obstacleGrid))
}
