package main

import(
  "fmt"
)

func main(){
  number := 1000
  isPrimeNumber(number)

}

func isPrimeNumber(number int){
  if number > 1{
    isPrime := true
    for i := 2; i < number; i++{
      if number % i == 0{
        isPrime = false
        break
      }
    }
    if isPrime{
      fmt.Printf("%d is a prime number", number)

    }else{
      fmt.Printf("%d is not a prime number", number)
    }
  }else{
    fmt.Println("Please enter a valid integer greater than 1")
  }
}
