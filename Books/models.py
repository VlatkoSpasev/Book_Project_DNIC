from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	year_of_birth = models.IntegerField()
	country = models.CharField(max_length=50)
	biography = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ("last_name", "first_name", "year_of_birth")

	def __str__(self):
		return self.first_name+" "+self.last_name


class Publication(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	address_1 = models.CharField(max_length=50)
	house_number = models.CharField(max_length=10)
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=50)	
	isbn = models.CharField(max_length=17)
	content = models.TextField(null=True, blank=True)
	cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class PublicationAuthor(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publication = models.ForeignKey(Publication, on_delete=models.CASCADE)