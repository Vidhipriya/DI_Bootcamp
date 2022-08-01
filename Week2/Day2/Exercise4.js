let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log(users.length)

if (users.length==0){
	console.log("no one is online")
}
else if (users.length==1) {
	console.log("<name_user> is online")
	
}
else if (users.length==2) {
	console.log("<name_user> and <name_user> is online")
	
}
else if (users.length>2) {
	console.log("<name_user>, <name_user>" , "and" , users.length , "online" )

}
