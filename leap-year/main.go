package main

import (
  "fmt"
)

func main() {
  fmt.Println(isLeapYear(2020))
  fmt.Println(isLeapYear(1999))
  fmt.Println(isLeapYear(2016))
  fmt.Println(isLeapYear(2400))
  fmt.Println(isLeapYear(2600))
  fmt.Println(isLeapYear(2021))
}


func isLeapYear(year int)(bool){
  if year % 4 == 0 && year % 100 !=0{
    return true;
  } else if year % 400 == 0{
    return true
  } else if year % 100 == 0{
    return false
  }
  return false
}
