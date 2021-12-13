const secretPersons = document.getElementsByClassName("secret-person")
const addSecret = document.getElementById("add-secret")
const secretForm = document.getElementById("secret-form")
let buttonCounter = 0

function deleteFuncion(e) {
	if (buttonCounter > 3) {
		this.parentNode.remove(this)
		buttonCounter--
	}
	else { 
		alert("At least 3 people required")
	}
}

function addFunction(e) {
	const newButton = document.createElement("button")
	newButton.classList.add("delete-button")
	newButton.setAttribute("type", "button")
	newButton.innerHTML = "❌"
	buttonCounter++
	newButton.addEventListener('click', deleteFuncion)

	const newSecret = document.createElement("div")
	newSecret.classList.add("secret-person")

	newSecret.innerHTML = `
	<label for="name${buttonCounter}" class="secret-label">Name</label>
	<input required type="text" name="name${buttonCounter}" class="secret-name" placeholder="Juanito Perez">
	<label for="email${buttonCounter}">Correo</label>
	<input required type="email" name="email${buttonCounter}" class="secret-email" placeholder="juanito.perez@email.com">
	`
	newSecret.appendChild(newButton)
	let childCounter = secretForm.childNodes.length - 5
	secretForm.insertBefore(newSecret, secretForm.childNodes[childCounter])
}

let currentButton
for (let i = 0; i < secretPersons.length; i++) {
	currentButton = secretPersons[i].childNodes[9]
	buttonCounter++
	currentButton.addEventListener('click', deleteFuncion)
}

addSecret.addEventListener('click', addFunction)