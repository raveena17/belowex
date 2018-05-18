from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# class User(models.Model):
# 	username = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)
# 	is_admin = models.BooleanField(default=False)

class Employee(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    recognition = models.CharField(max_length=255,null=True )
    gender = models.CharField(max_length=6, null=True)
    mail_id = models.EmailField(max_length=300, null=True)
    date_of_birth = models.DateField(null=True)
    create_date = models.DateField(null=True)

    def get_absolute_url(self):
    	return reverse('mymail:index')
