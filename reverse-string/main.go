package main

import(
  "fmt"
)

func main(){

  word := "I need a job!"
  fmt.Println(reverseString(word))

}

func reverseString(originalString string)(string){
  newString := ""
  for i := len(originalString) - 1; i >= 0; i--{
    newString = newString + string(originalString[i])
  }
  return newString
}
