from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
#from django.utils import timezone



class Employee(models.Model):

    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    mail_id = models.EmailField(max_length=300)
    date_of_birth = models.DateField()
    
    def __str__(self):     
        return self.name

    def get_absolute_url(self):
        return reverse('mymail:index')


class Meta:
    verbose_name_plural = "employees"


    