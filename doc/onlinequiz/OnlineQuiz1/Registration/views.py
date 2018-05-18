from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Attendee
from django.utils import timezone
from django.shortcuts import redirect

#class RegistrationView:

def view_homepage(request):
    postlist = Attendee.objects.all()
    context = {'postlist': postlist}
    return render(request, 'home.html',{'postlist':postlist})


def get_value(request):
    return render(request,'register1.html')
    
def add_attendee_detail(request):
    name = request.POST.get('name')
    qualification = request.POST.get('qualification')
    age = request.POST.get('age')
    phoneNo = request.POST.get('mailId')
    mailId = request.POST.get('mailId')
    address = request.POST.get('address')
    date_of_birth = request.POST.get('date_of_birth')
    gender = request.POST.get('gender')
    language = request.POST.get('language')
    Attendee.objects.create(name = name, qualification = qualification, age = age, phoneNo = phoneNo, mailId = mailId, address = address, date_of_birth = date_of_birth, gender = gender, language = language)
    return ("successfully")

    # name = request.POST.get('name')
    # date_of_birth = request.POST.get('date_of_birth')
    # mail_id = request.POST.get('mail_id')
    # address = request.POST.get('address')
    # mobile_no = request.POST.get('mobile_no')
    # Attendee.objects.create(name = name, date_of_birth = date_of_birth, mail_id = mail_id, address = address, mobile_no = mobile_no)
    # return ("successfully")
