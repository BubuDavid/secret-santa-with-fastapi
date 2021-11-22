# Python
import starlette.status as status
from functions.functions import randomizer, send_secret_santas
from models.person import Person
# main.py
from fastapi import FastAPI, Body, Request, responses

# Application
app = FastAPI() # FastAPI instance

# Unique endpoint
@app.post("/secret-santa")
async def secret_post(request: Request):
	# Get the data from the form
	form_data = await request.form()
	url = request.headers['referer']
	# This data is in a weird dictionary so 
	# we need to clean it and put it in other form
	names = ["" for _ in range(len(form_data.items())//2)]
	emails = ["" for _ in range(len(form_data.items())//2)]
	people = []
	
	for key, value in form_data.items():
		pos = int(key[-1])
		if 'name' in key:
			names[pos] = value
		else:
			emails[pos] = value
	# The people has the form [Person, Person, Person]
	# And each Person is an object.
	for name, email in zip(names, emails):
		people.append(Person(name, email))

	# Set the random givers (So random people that gives other random people)
	randomizer(people)
	# Print the persons to know everything is fine
	# for person in people:
	# 	print(person)
	
	# Send the emails with the relations given by relations
	send_secret_santas(people)

	return responses.RedirectResponse(url = f'{url}secret-santa/success', status_code=status.HTTP_302_FOUND)