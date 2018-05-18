from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.db import IntegrityError
from .models import Attendee, Question, Choice
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect


# def view_homepage(request):
#     postlist = Attendee.objects.all()
#     context = {'postlist': postlist}
#     return render(request, 'home.html',{'postlist':postlist})

def view_homepage(request):
    return render(request, 'home.html')

def attendee_register(request):
    return render(request,'register_form.html')

def view_language(request):
    return render(request, 'language.html')
    
def add_attendee(request):
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

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

# def count(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         #selected_choice.counts += 1
#         # selected_choice.save()
#         return HttpResponseRedirect(reverse('Registration:results', args=(question.id,)))




def get_next_id(request, curr_id):
    try:
        res = Question.objects.filter(id__gt=curr_id).order_by("id")[0:1].get().id
    except Question.DoesNotExist:
        res = Question.objects.aggregate(Min("id"))['id__min']
    return res

def get_prev_id(request, curr_id):
    try:
        res = Question.objects.filter(id__lt=curr_id).order_by("-id")[0:1].get().id
    except Question.DoesNotExist:
        res = Question.objects.aggregate(Max("id"))['id__max']
    return res






































# def next(request, question_id):
#     next_question = Question.objects.filter(title=title).filter(number__gt=question.number).order_by('number')[0:1]





# def next(request, question_id):
#     next_question = (Question.objects
#     .filter(number__gte=question.number, id__gt=instance.id)
#     .exclude(id=question.id)
#     .order_by('number', 'id')
#     .first())

# def previous(request, question_id):
#     prev_question = (Question.objects
#     .filter(number__lte=question.number, id__lt=instance.id)
#     .exclude(id=question.id)
#     .order_by('-number', '-id')
#     .first())
