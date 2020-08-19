function reverseString(originalString){
  if(typeof originalString === "string"){
    let reversedString = "";

    for(let i = originalString.length - 1; i >= 0; i--) {
      reversedString += originalString[i];
    }

    return reversedString;
  }
  else{
    return "Please enter a valid string"
  }
}

let word = "I need a job!";

console.log(reverseString(word));
