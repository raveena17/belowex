from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Attendee, Question, Choice
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect


# # def view_homepage(request):
# #     postlist = Attendee.objects.all()
# #     context = {'postlist': postlist}
# #     return render(request, 'home.html',{'postlist':postlist})

# def view_homepage(request):
#     return render(request, 'home.html')


# def attendee_register(request):
#     return render(request,'register_form.html')
    
# def add_attendee(request):
#     name = request.POST.get('name')
#     qualification = request.POST.get('qualification')
#     age = request.POST.get('age')
#     phoneNo = request.POST.get('mailId')
#     mailId = request.POST.get('mailId')
#     address = request.POST.get('address')
#     date_of_birth = request.POST.get('date_of_birth')
#     gender = request.POST.get('gender')
#     language = request.POST.get('language')
#     Attendee.objects.create(name = name, qualification = qualification, age = age, phoneNo = phoneNo, mailId = mailId, address = address, date_of_birth = date_of_birth, gender = gender, language = language)
#     return ("successfully")

class IndexView(generic.ListView):                
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter( pub_date__lte=timezone.now()).order_by('-pub_date')[:5]     # <------


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

