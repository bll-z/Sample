from django.db import models
from django import forms
from django.forms import ModelForm

class Genre(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published')
	writers = models.ManyToManyField(Author)
	genre = models.ForeignKey(Genre)
	def __unicode__(self):
		return self.title

class GenreForm(ModelForm):
	class Meta: 
		model = Genre
		fields = ['name'] 

class AuthorForm(ModelForm):
	class Meta: 
		model = Author
		fields = ['name'] 

class BookForm(ModelForm):
	class Meta: 
		model = Book
		fields = ['title','writers','pub_date','genre'] 