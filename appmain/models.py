from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	
