from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import template
from django.template.loader import render_to_string

from bookshelf.models import Book,BookForm,Author,AuthorForm,Genre,GenreForm

def index(request):
	return render(request, 'bookshelf/index.html', {})

class BooksView(generic.ListView):
	template_name = 'bookshelf/books.html'
	context_object_name = 'book_list'
	def get_queryset(self):
		"""Return a list of all the books"""
		return Book.objects.all()

class BookView(generic.DetailView):
	model = Book
	template_name = 'bookshelf/book.html'

def createBook(request):
	if request.method == 'POST': 
		form = BookForm(request.POST) 
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/bookshelf/')
	else:
		form = BookForm()
	return render(request, 'createBook.html', {
		'form': form,
	})

def createAuthor(request):
	if request.method == 'POST': 
		form = AuthorForm(request.POST) 
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/bookshelf/')
	else:
		form = AuthorForm() 

	return render(request, 'createAuthor.html', {
		'form': form,
	})

def createGenre(request):
	if request.method == 'POST': 
		form = GenreForm(request.POST) 
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect('/bookshelf/')
	else:
		form = GenreForm() 

	return render(request, 'createGenre.html', {
		'form': form,
	})