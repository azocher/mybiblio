from django.forms import ModelForm

from appmain.models import Book

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ('name', 'description',)