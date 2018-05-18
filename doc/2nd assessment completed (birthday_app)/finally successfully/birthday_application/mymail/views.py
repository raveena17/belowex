from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Employee
from django.utils import timezone
from django.shortcuts import redirect



def view_admindetail(request):
    postlist = Employee.objects.all()
    context = {'postlist': postlist}
    return render(request, 'administerdetail.html',{'postlist':postlist})

def get_value(request):
    return render(request,'get.html')
    
def add_employee(request):
        name = request.POST.get('name')
        recognition = request.POST.get('recognition')
        gender = request.POST.get('gender')
        mail_id = request.POST.get('mail_id')
        date_of_birth = request.POST.get('date_of_birth')
        create_date = request.POST.get('create_date') 
        Employee.objects.create(name = name, recognition = recognition, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth, create_date = create_date)
        return redirect('/mymail/')

def delete(request, id):
    employee = Employee.objects.filter(pk = id).delete()
    return redirect('/mymail/')

def find_birthday(request):
    today = timezone.now().date()
    employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month)  
    return render(request, 'birthday_list.html', {'employee_details': employee})


       










        # Employee.objects.create(name = name, recognition = recognition, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth, create_date = create_date)
        # except IntegrityError as e:
        #   return HttpResponse('please provide full details')


        # if IntegrityError:
        #     return HttpResponse('please provide full details')
        # else:
        #     Employee.objects.create(name = name, recognition = recognition, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth, create_date = create_date)
        #     return redirect('/mymail/')



        #return HttpResponse('please provide full details')
           
    #     if name=='' or recognition=='' or gender=='' or mail_id=='' or date_of_birth=='' or create_date=='':
    #         return HttpResponse('please provide full details')
    #     else:
    #         Employee.objects.create(name = name, recognition = recognition, gender = gender, mail_id = mail_id, date_of_birth = date_of_birth, create_date = create_date)
    #     return redirect('/mymail/')
    # except AttributeError:
    #     pass








