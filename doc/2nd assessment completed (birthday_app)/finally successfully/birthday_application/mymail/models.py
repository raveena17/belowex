from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Employee(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    recognition = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    mail_id = models.EmailField(max_length=300)
    date_of_birth = models.DateField()
    create_date = models.DateField(auto_now=True)

    def get_absolute_url(self):
    	return reverse('mymail:index')
