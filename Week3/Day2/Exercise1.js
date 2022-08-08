function insertRow(){
   	  let count=count+1
   	 document.getElementsById("sampleTable")
   	 let row=document.createElement("tr")
   	 row.innerHTML="<td>Row2 cell1</td>"+ count +"  <td>Row2 cell2</td>" 
   	 table.appendChild(row)

}