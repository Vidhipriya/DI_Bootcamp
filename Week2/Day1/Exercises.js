let favourite="chocolate";
let meal="breakfast";
console.log("I eat"+" " + favourite+" at every "+meal)

let myWatchedSeries = ["superman","black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength=myWatchedSeries.length;
let myWatchedSeriesSentence= "black mirror,money heist, the big bang theory"
console.log("I watched"+ myWatchedSeriesLength +"series"+":"+myWatchedSeriesSentence)
myWatchedSeries.indexOf("the big bang theory")
// myWatchedSeries.splice(myWatchedSeries.indexOf("the big bang theory"),1)
myWatchedSeries[myWatchedSeries.indexOf("the big bang theory")]= "Friends"
console.log(myWatchedSeries)
myWatchedSeries.push("Breaking Bad")
console.log( myWatchedSeries)
myWatchedSeries.unshift("Avatar")
console.log(myWatchedSeries)
myWatchedSeries.indexOf("money heist")
myWatchedSeries.splice(myWatchedSeries.indexOf("black mirror"),1)
console.log( myWatchedSeries)
myWatchedSeries.indexOf("3")
myWatchedSeries[myWatchedSeries.indexOf("money heist")].substring(2, 3)
console.log(myWatchedSeries[myWatchedSeries.indexOf("money heist")].substring(2, 3))
console.log(myWatchedSeries)

// The temperature converter
let temperature_C= 30;
let temperature_F= temperature_C/5*9+32
console.log(temperature_F) 

// Guess The Answers
let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:55
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:23
    // Actual:23


    // Guess the answers2

    typeof(15)

// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:number
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:true
// Actual:true

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:hamburger
// Actual:NaN

"1" + "3"
// Prediction:4
// Actual:4

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:JOHNNY5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction:
// Actual:NaN

1 != 1
// Prediction:False
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:False
// Actual:False

// Guess Exercise 3

5 + "34"
// Prediction:39
// Actual:534

5 - "4"
// Prediction:
// Actual:1

10 % 5
// Prediction:0.5
// Actual:0

5 % 10
// Prediction:5

// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:

" " + " "
// Prediction:
// Actual:

" " + 0
// Prediction:0
// Actual:

true + true
// Prediction:
// Actual:2

true + false
// Prediction:0
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:-1
// Actual:-1

!true
// Prediction:
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:
// Actual:NaN


