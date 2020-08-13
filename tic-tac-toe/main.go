package main

import (
  "fmt"
)

func main() {
  board := make(map[int]string)
  gameOver := false

  for i := 1; i <= 9; i++ {
    board[i] = fmt.Sprintf("%d", i)
  }

  printBoard(board)

  playGame(board, gameOver)

  fmt.Println("Game Over!")

}

func printBoard(board map[int]string) {
  fmt.Println(board[1], board[2], board[3])
  fmt.Println(board[4], board[5], board[6])
  fmt.Println(board[7], board[8], board[9])
}

func playGame(board map[int]string, gameOver bool) {
  for gameOver == false {
    var space int
    fmt.Print("Enter the space you want to play: ")
    fmt.Scan(&space)
    var letter string
    fmt.Print("Enter your letter: ")
    fmt.Scan(&letter)

    board[space] = letter
    printBoard(board)
    gameOver = winConditionMet(board)
  }

}

func winConditionMet(board map[int]string) bool {
  if board[1] == board[2] && board[2] == board[3]{
    return true
  }
  if board[4] == board[5] && board[5] == board[6]{
    return true
  }
  if board[7] == board[8] && board[8] == board[9]{
    return true
  }
  if board[1] == board[4] && board[4] == board[7]{
    return true
  }
  if board[2] == board[5] && board[5] == board[8]{
    return true
  }
  if board[3] == board[6] && board[6] == board[9]{
    return true
  }
  if board[1] == board[5] && board[5] == board[9]{
    return true
  }
  if board[3] == board[5] && board[5] == board[7]{
    return true
  }
  return false
}
