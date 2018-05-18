from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Employee
from django.utils import timezone
from django.shortcuts import redirect


def view_homepage(request):
    return render(request, 'home.html')


def view_employee_list(request):
    postlist = Employee.objects.all()
    context = {'postlist': postlist}
    return render(request, 'employee_details.html', {'postlist': postlist})


def employee_register(request):
    return render(request, 'register.html')


def add_employee(request):
    # import pdb;pdb.set_trace()
    name = request.POST.get('name')
    designation = request.POST.get('designation')
    gender = request.POST.get('gender')
    mail_id = request.POST.get('mail_id')
    date_of_birth = request.POST.get('date_of_birth')
    Employee.objects.create(
        name=name,
        designation=designation,
        gender=gender,
        mail_id=mail_id,
        date_of_birth=date_of_birth)
    return redirect('/birthday/employee_list/')

    # try:
    #     Employee.objects.create(name = name, designation = designation, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth)
    #     return HttpResponse(status=201)
    # except Exception as e:
    #     return HttpResponse(status=500)


def delete_employee(request):
    _id = request.GET['id']
    employee = Employee.objects.get(pk=_id)
    employee.delete()
    return HttpResponse(employee.name + "   " + "record deleted")


def get_employee_by_birthday(request):
    today = timezone.now().date()
    employee = Employee.objects.filter(
        date_of_birth__day=today.day,
        date_of_birth__month=today.month)
    return render(
        request, 'birthday_list.html', {
            'employee_details': employee})


# def add_employee(request):
    # data = request.POST.dict()
    # print data
    # try:
    #     Employee.objects.create(**data)
    #     return HttpResponse(status=201)
    # except Exception as e:
    #     return HttpResponse(status=500)
