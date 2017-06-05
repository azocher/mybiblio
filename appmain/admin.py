from django.contrib import admin

# import dem models
from appmain.models import Book

# auto slug creation for model
class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ('name', 'author', 'description',) 
	prepopulated_fields = {'slug': ('name',)}

# register dem models
admin.site.register(Book, BookAdmin)
