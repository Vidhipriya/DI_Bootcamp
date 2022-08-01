// Exercise 1 : Divisible By Three
let numbers = [123, 8409, 100053, 333333333, 7]
for (let number of numbers){
   if ( number/3){

   	console.log("true")
   }
   else {
   	console.log("false")
   	
   }

};
// Exercise 2 : Attendance
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}
for (let x in guestList)
prompt("Give me your name",)

if (guestList[x]){
	console.log("Hi! I'm" + x + "I'm from" + guestList[x])
}
else{

	console.log("Hi! I'm a guest.")
}

// Exercise 3 : Playing With Numbers
let age = [20,5,12,43,98,55];
let sum=0;
for(let value of age){
	sum+= value;
}
console.log(sum);