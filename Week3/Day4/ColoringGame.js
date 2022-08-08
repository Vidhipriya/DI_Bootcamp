
let buttoner=document.getElementById("lebutton")
buttoner.addEventListener("click", onclick)
 function onclick (e) {
  e.target.style.display= ""
 }

 let full =document.getElementsByTagName("body")
full= full.addEventListener("mouseup",onMouseUp)
 function onMouseUp(){
 	mousedown=false
 }
 full=full.addEventListener("mousedown",onMouseDown)
 function onMouseDown (){
 	mouseup=false
 }

let toColor=document.getElementById("coloring")
toColor.addEventListener("dragstart",onDragStart)
function onDragStart(e){

}
let colored=document.getElementById("blank")
colored.addEventListener("dragend",)