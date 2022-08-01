
let addressStreet= " BenYehuda";
let addressNumber=  "5";
let country="Israel"
let globalAddress= "I live in"+" " +addressNumber+ addressStreet+ " " +country;
console.log(globalAddress)

let birthYear="2003";
let futureYear="2022";
let age="19";
console.log("I will be"+" " + age + " " +  "in" + " "  + futureYear)

let pets=["cats" ,"dogs" ,"rabbits","hamster","fish"];
let best=pets[1];
console.log(best)
pets.push("horse")
console.log(pets)
pets.splice(2,1)
console.log(pets)
console.log(pets.length)