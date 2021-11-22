from models.person import Person
import random
import smtplib, ssl
from decouple import config

def randomizer(people: list[Person]) -> None:
	emails = []
	for person in people:
		emails.append(person.email)

	email_reference = emails.copy()
	loop = True
	while loop:
		emails = email_reference.copy()
		giving_emails = emails.copy()
		loop = False
		for pos, reference in enumerate(email_reference):
			giving_emails[pos] = emails.pop(random.randint(0, len(emails)-1))
			if giving_emails[pos] == reference:
				loop = True
				break

	for person, giving in zip(people, giving_emails):
		person.giving = giving

	return people


def send_secret_santas(people: list[Person]):
	port = 465  # For SSL
	password = config('EMAIL_PASSWORD')
	email = config('EMAIL')

	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(email, password)
		for person in people:
			receiver_email = person.email
			for search in people:
				if search.giving == receiver_email:
					name = search.name
					break
			message = f"""
Hola! Te toca {name}, feliz navidad y joto el que lo lea.
			"""
			
			server.sendmail(email, receiver_email, message)