
// Exercise 1 : List Of People
let people = ["Greg", "Mary", "Devon", "James"];
people.shift()
people.splice(3,1,"Jason")
people.push("Vidhipriya")
people.indexOf("Mary")
// Mary , devon ,jason,vidhipriya
// 0     , 1    ,  2   ,3
//-4 ,     -3   ,    -2  ,-1
console.log(people.slice(1,-1))
people.indexOf("Foo")
let last =people[people.length -1]
console.log(last)
for (let x in people)
{
	console.log(people[x])
if(people[x] == "Jason")
{
	break;
}}




// Exercise 2 : Your Favorite Colors 
let colors=["red","blue","yellow","green","brown"];
for (let x in colors)
	if (x == 0){

		continue;

	}
	 else
    {console.log("My #" + x + " choice is " + colors[x])}
	


// Exercise 3 : Repeat The Question
let user=Number(prompt('Give me a number',1))
   
   while (user < 10) {
   console.log('Give me another number',)
   }
    else{
    	console.log('it good')

    }
   

  // Exercise 4 : Building Management
  let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor)
console.log(building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[1] + building.numberOfRoomsAndRent.dan[0] )

if( building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1])
{
	console.log(building.numberOfRoomsAndRent.dan[1] +1200)
	building.numberOfRoomsAndRent.dan[1]=building.numberOfRoomsAndRent.dan[1] +1200
}



// Exercise 5 : Family
let family ={
	mom:"Jane"

	dad:"Jack"

	child:"Jack"
	};
for ( let i in family) 
{console.log(family[i])}
{console.log(family)}

// Exercise 6
let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'};
  let str=""
  for (let x in details ){
  	str= str + x + " "+details[x] +""
  	console.log(str)
}
// Exercise 7 : Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let firstStr = []
for(name of names ){
	firstStr.push(name.charAt(0))

}
firstStringChar=firstStr.sort()

firstStringChar=firstStr.join("")

console.log(firstStr)

