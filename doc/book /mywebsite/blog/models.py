from __future__ import unicode_literals
from django.db import models


class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	is_admin = models.BooleanField(default=False)

class Book(models.Model):
	book_name = models.CharField(max_length=200)
	book_author = models.CharField(max_length=300)
	#comment = models.CharField(max_length=700,blank=True,null=True)

class Comment(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE) 
	comment = models.CharField(max_length=700, blank=True, null=True)
	#total = models.IntegerField(default=0)