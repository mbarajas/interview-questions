function isLeapYear(year){
  if(year % 4 === 0 && year % 100 !==0){
    return true;
  }
  else if(year % 400 === 0){
    return true;
  }
  else if(year % 100 === 0){
    return false;
  }
  return false;
}

console.log(isLeapYear(2020));
console.log(isLeapYear(1999));
console.log(isLeapYear(2016));
console.log(isLeapYear(2400));
console.log(isLeapYear(2600));
console.log(isLeapYear(2021));
