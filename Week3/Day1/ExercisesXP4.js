let allBooks=[]
allBooks.push({
	title:"The Poisonwood Bible",
	author:"Barbara Kingsolver",
	image:"https://www.oca.ac.uk/wp-content/uploads/2020/08/9780571298846-uk.jpg",
	alreadyRead:true
})
allBooks.push({
	title:"An experiment with an airpump",
	author:"Shelagh Sthepehnson",
	image:"https://www.whsmith.co.uk/mobify/caching/assets/product-image/large/9780413733108-10-000_1.jpg",
	alreadyRead:false
})
// document.createElement('table')
 let newTable = document.createElement('table')
 allBooks=allBooks.append(newTable)  
