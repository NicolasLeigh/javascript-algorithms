package main

import "fmt"

// countBattleships counts the number of battleships on the board.
func countBattleships(board [][]byte) int {
	m, n, count := len(board), len(board[0]), 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == '.' {
				continue
			}
			if i > 0 && board[i-1][j] == 'X' {
				continue
			}
			if j > 0 && board[i][j-1] == 'X' {
				continue
			}
			count++
		}
	}

	return count
}

func main() {
	board := [][]byte{
		{'X', '.', '.', 'X'},
		{'.', '.', '.', 'X'},
		{'.', '.', '.', 'X'},
	}
	result := countBattleships(board)
	fmt.Println(result) // Output: 2
}
