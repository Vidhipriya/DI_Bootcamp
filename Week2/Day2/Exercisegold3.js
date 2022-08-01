 let verb = prompt("Please enter verb")
   let verb1 = verb.toLowerCase()
   let n =verb1.length
   let str = verb1;
   let part = /ing/i;
   let result = str.match(part);
   
console.log(result)
if (n <3){
console.log(verb1)

}
else if (n >3 &&  result != null )
console.log(verb1+"ly")
else 
console.log(verb1 + "ing")