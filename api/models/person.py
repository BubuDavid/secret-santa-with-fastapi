class Person:
	def __init__(self, name, email, giving=None) -> None:
		self.name = name
		self.email = email
		self.giving = giving

	def __str__(self) -> str:
		return str({
			'name': self.name,
			'email': self.email,
			'giving': self.giving,
		})