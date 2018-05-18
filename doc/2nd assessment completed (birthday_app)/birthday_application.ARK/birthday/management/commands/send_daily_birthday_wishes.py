# birthday/management/commands/send_daily_birthday_wishes.py
"""
Custom management command that sends an email to all users
born on the current day and month.
"""
from django.core.management import BaseCommand
from django.core.mail import send_mail
from birthday.models import Employee
from django.utils import timezone

class BirthdayGreetings(BaseCommand):
    #send mail to all employees and birthday employees

    def send_birthday_alert_mail(self, **options):
        today = timezone.now().date()
        birthday_list = Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)
        if len(birthday_list) != 0:
            for emp in birthday_list:
                subject = 'BIRTHDAY GREETINGS '
                message = 'TODAY IS ** %s ** BIRTHDAY!' % emp.name
                from_email = 'raveena@5gindia.net'
                recipients = Employee.objects.exclude(id=emp.id).values_list('mail_id', flat=True)
                send_mail(subject, message, from_email, recipients, fail_silently=False)            
                
                message1 = 'HAPPY BIRTHDAY ** %s **!' % emp.name
                recipients1 = Employee.objects.filter(id=emp.id).values_list('mail_id', flat=True)
                send_mail(subject, message1, from_email, recipients1, fail_silently=False)            



                 # (or)
# send mail to all employees except birthday employees

#     def handle(self, **options):
#         today = timezone.now().date()
#         birthday_list = Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)
#         if len(birthday_list) != 0:
#             for emp in birthday_list:
#                 subject = 'BIRTHDAY LIST '
#                 message = 'TODAY IS ** %s ** BIRTHDAY!' % emp.name
#                 from_email = 'raveena@5gindia.net'
#                 recipients = Employee.objects.exclude(id=emp.id).values_list('mail_id', flat=True)
#                 send_mail(subject, message, from_email, recipients, fail_silently=False)            


    


