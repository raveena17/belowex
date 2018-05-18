from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Employee(models.Model):

    name = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    mail_id = models.EmailField(max_length=300, null=False)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Meta:
    verbose_name_plural = "employees"
