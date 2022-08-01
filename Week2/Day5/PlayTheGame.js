function playTheGame(){
	confirm("Would you like to play the game?")
	do (answer=false) {
		alert("No problem, Goodbye")
	}
    while(answer=true){
    	number(prompt("Enter a number between 0 and 10", 0))
    }

}