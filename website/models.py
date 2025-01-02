from django.db import models


class Book(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	status = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)
	genre = models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.title}")

