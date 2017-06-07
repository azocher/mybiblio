from django.shortcuts import render, redirect
from appmain.models import Book
from appmain.forms import BookForm


# MAH VIEWS ALL DEM VIEWS VIEWS FROM THE SIX

def index(request):
	
	# define book 
	books = Book.objects.all()
	
	# main view
	return render(request, 'index.html', {
		'books' : books, 
		})
		
def book_detail(request, slug):
	# grab object
	book = Book.objects.get(slug=slug)
	
	# pass object to template
	return render(request, 'books/book_detail.html', {
		'book': book,
	})
	
def edit_book(request, slug):
	# grab object
	book = Book.objects.get(slug=slug)
	
	# form decl
	form_class = BookForm
	
	 
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('book_detail', slug=book.slug)
	else:
		form = form_class(instance=book)
		return render(request, 'books/edit_book.html', {
			'book': book,
			'form': form,
		})
	
	
	