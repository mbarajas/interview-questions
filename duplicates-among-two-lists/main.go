package main

import(
  "fmt"
  "sort"
)

func main(){
  var listOne []int= []int{1,2,3,4,5,6,7,8,9,2}
  var listTwo []int= []int{2,4,6,8,10,12,4,16,20}

  fmt.Println(findDuplicates(listOne, listTwo))

}

func findDuplicates(listOne []int, listTwo []int)(duplicateList []int){
  for i:= 0; i < len(listOne); i++{
    for j:= 0; j < len(listTwo); j++{
      if listTwo[j] == listOne[i]{
        duplicateList = append(duplicateList, listTwo[j])
      }
    }
  }
  sort.Ints(duplicateList)
  return duplicateList
}
