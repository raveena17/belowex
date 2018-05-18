# polls/management/commands/send_daily_birthday_wishes.py
"""
Custom management command that sends an email to all users
born on the current day and month.
"""
from django.core.management import BaseCommand
from django.core.mail import send_mail
from mymail.models import Employee
from django.utils import timezone
#from someplace import User

class Command(BaseCommand):

    def handle(self, **options):
        today = timezone.now().date()
        # for emp in Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month):
        #     subject = 'BIRTHDAY WISHES'
        #     body = '** HAPPY BIRTHDAY ** %s!' % emp.name
        #     send_mail(subject, body, 'raveena@5gindia.net', [emp.mail_id])
        #     rint employees.count()
        #     if employees.count() !=0 :
        for employees in Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month):
            subject = 'BIRTHDAY WISHES'
            body = 'HAPPY BIRTHDAY ** %s **!' % employees.name
            send_mail(subject, body, 'raveena@5gindia.net', [employees.mail_id])
            for employee in Employee.objects.exclude(date_of_birth__day=today.day, date_of_birth__month=today.month):
                birthday_employee =  employees.name
                #subject = 'Happy birthday %s!' % employee.name
                subject = 'BIRTHDAY LIST '
                body = 'TODAY IS **  %s  ** BIRTHDAY!' % birthday_employee
                send_mail(subject, body, 'raveena@5gindia.net', [employee.mail_id])