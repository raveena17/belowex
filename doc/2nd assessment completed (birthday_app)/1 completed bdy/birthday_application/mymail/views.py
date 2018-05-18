from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
#from django.core.mail import send_mail
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Employee
#from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone

class IndexView(View):
    context_object_name = 'employee_list'
    def get(self, request, *args, **kwargs):
            emp =  Employee.objects.all()
            # print emp
            return render(request, 'index.html', {'employees': emp})

    # def get_queryset(request):
    #     emp =  Employee.objects.all()
    #     return render(request, 'index.html' , {'employee': emp})


class EmployeeEntry(CreateView):
    model = Employee
    fields = ['name', 'recognition', 'gender', 'mail_id', 'date_of_birth', 'create_date']

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'recognition', 'gender', 'mail_id', 'date_of_birth', 'create_date']

class EmployeeDelete(DeleteView):
    model = Employee
    sucess_url = reverse_lazy('mymail:index')





# def find_birthday(request):
#     today = timezone.now().date()
#     # print today
#     employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month)  
#     #employee = Employee.objects.filter(date_of_birth__day = today.day, date_of_birth__month=today.month) ==>display birthday persons name list
#     # print employee[0].name
#     return render(request, 'birthday_list.html', {'employee': employee})



# #@csrf_exempt
# def index(request):
     
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         recognition = request.POST.get('recognition')
#         gender = request.POST.get('gender')
#         mailid = request.POST.get('mailid')
#         dateofbirth = request.POST.get('dateofbirth')
 		
#         context = {
#             'name': name,
#             'recognition': recognition,
#             'gender': gender,
#             'mailid': mailid,
#             'dateofbirth': dateofbirth
#         }
        
#         template = loader.get_template('showdata.html')
#         return HttpResponse(template.render(context, request))
#     else: 
#         template = loader.get_template('index.html')
#         return HttpResponse(template.render())







