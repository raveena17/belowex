view.py












#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail
from . models import Employee

from django.utils import timezone


def today_birthday_babies(request):
	today = timezone.now().date()
	# print today
	employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month)
	#employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month) ==>display birthday persons name list
	# print employee[0].name
	return render(request, 'birthday_list.html', {'employee': employee})

def others(request):
	today = timezone.now().date()
	employee = Employee.objects.exclude(date_of_birth__day = today.day, date_of_birth__month=today.month)
	# display without birthday persons name_list
	return render(request, 'birthday_list.html', {'employee': employee})

