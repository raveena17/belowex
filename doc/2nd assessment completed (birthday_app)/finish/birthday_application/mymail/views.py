from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Employee
from django.utils import timezone
from django.shortcuts import redirect


def view_home(request):
    return render(request, 'home.html')

def view_employee_list(request):
    postlist = Employee.objects.all()
    context = {'postlist': postlist}
    return render(request, 'administerdetail.html',{'postlist':postlist})

def employee_register(request):
    return render(request,'get.html')
    
def add_employee(request):
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        mail_id = request.POST.get('mail_id')
        date_of_birth = request.POST.get('date_of_birth')
        Employee.objects.create(name = name, designation = designation, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth)
        return redirect('/mymail/employee_list/')

def delete(request, id):
    employee = Employee.objects.filter(pk = id).delete()
    return redirect('/mymail/employee_list/')

def edit(request, id):
    employee = Employee.objects.filter(pk = id).edit()
    return redirect('/mymail/employee_list/')

def find_birthday(request):
    today = timezone.now().date()
    employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month)  
    return render(request, 'birthday_list.html', {'employee_details': employee})


       















