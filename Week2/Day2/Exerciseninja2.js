let zipcode=prompt('What is your zip code?', 0)
if (zipcode===/[0-9]{5,5}\S/ && zipcode.length<6){
	alert('success!')
}
else{
	alert('error')
}