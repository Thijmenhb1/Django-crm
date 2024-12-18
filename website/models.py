from django.db import models



class Client(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	zip_code = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")



class Ticket(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	last_updated = models.DateTimeField(auto_now = True)
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 500)
	status = models.CharField(max_length = 50)
	priority = models.CharField(max_length = 50)
	notes = models.CharField(max_length = 2000)

	def __str__(self):
		return f"Ticket: {self.title}, Status: {self.status}"






