var defoultHeightProductBlock = 10
let idValues = [40, 40, 40, 40, 40, 40, 40]
function change_height(id)
	 {
	 var container=document.getElementById(id);
	 var button = document.getElementById("button"+id);
	 //alert(container.style.maxHeight)
	 if((container.style.maxHeight === (defoultHeightProductBlock+"rem")) || (container.style.maxHeight === ""))
	 {
		button.innerText = "Скрыть";
		container.style.maxHeight= idValues[Number(id)]+"rem"
	 }
	 else
	 {
		button.innerText = "Подробнее";
		container.style.maxHeight = defoultHeightProductBlock+"rem"
	 }
	 }
