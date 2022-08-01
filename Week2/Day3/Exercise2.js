let names= ["john", "sarah", 23, "Rudolf",34]
for (let i in names)
	{if (typeof(names[i])!="string"){
		continue;
	}
	else if(typeof(names[i])=="string"){ 
	 names[i]=names[i].charAt(0).toUpperCase()

	console.log(names[i])	
	}if(names[x])

	
}