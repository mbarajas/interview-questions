function findDuplicates(listOne, listTwo){

  let duplicateCounter = [];
  let i;
  let j;

  for(i in listOne){
    for(j in listTwo){
      if(listTwo[j] === listOne[i]){
        duplicateCounter.push(listTwo[j]);
      }
    }
  }
  return duplicateCounter.sort();
}

let listOne = [1,2,3,4,5,6,7,8,9,2];
let listTwo = [2,4,6,8,10,12,4,16,20];
console.log(findDuplicates(listOne,listTwo));
