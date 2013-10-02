from django.conf.urls import patterns, url

from bookshelf import views

urlpatterns = patterns('',
	# ex: /bookshelf
	url(r'^$', views.index, name='index'),
    # ex: /bookshelf/book/book_id
    url(r'^book/(?P<pk>\d+)$', views.BookView.as_view(), name='book'),
    # ex: /bookshelf/books/
	url(r'^books/$', views.BooksView.as_view(), name='books'),
	# ex: /bookshelf/createBook/
	url(r'^createBook/$', views.createBook, name='createBook'),
	url(r'^createAuthor/$', views.createAuthor, name='createAuthor'),
	url(r'^createGenre/$', views.createGenre, name='createGenre'),
)