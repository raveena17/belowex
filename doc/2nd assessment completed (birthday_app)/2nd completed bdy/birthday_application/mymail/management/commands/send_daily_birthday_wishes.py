# polls/management/commands/send_daily_birthday_wishes.py
"""
Custom management command that sends an email to all users
born on the current day and month.
"""
from django.core.management import BaseCommand
from django.core.mail import send_mail
from mymail.models import Employee
from django.utils import timezone

class Command(BaseCommand):

#send mail to all employees except birthday employees
    # def handle(self, **options):
    #     today = timezone.now().date()
    #     birthday_list = Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)
    #     if len(birthday_list) != 0:
    #         for emp in birthday_list:
    #             subject = 'BIRTHDAY LIST '
    #             message = 'TODAY IS ** %s ** BIRTHDAY!' % emp.name
    #             from_email = 'raveena@5gindia.net'
    #             recipients = Employee.objects.exclude(id=emp.id).values_list('mail_id', flat=True)
    #             send_mail(subject, message, from_email, recipients, fail_silently=False)            


    #                  (or)


#send mail to all employees and birthday employees
    def handle(self, **options):
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








#     mail_list = [employee.encode("utf8") for employee in Employee.objects.values_list('mail_id', flat=True)]
#     print mail_list   # all employees mail_id printed but avoid [u] - in -> [u'string']
        
#     mail_list = [employees.encode("utf8") for employees in Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month).values_list('mail_id', flat=True)]
#     print mail_list    # only birthday_person print 



#     def handle(self, **options):
#         today = timezone.now().date()
#         for employees in Employee.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month):
#             subject = 'BIRTHDAY WISHES'
#             body = 'HAPPY BIRTHDAY ** %s **!' % employees.name
#             send_mail(subject, body, 'raveena@5gindia.net', [employees.mail_id])
            
#             mail_list = []
#             for employee in Employee.objects.exclude(date_of_birth__day=today.day, date_of_birth__month=today.month):
#                 mail_list.append(employee.mail_id)
#                 if mail_list:
#                     birthday_employee =  employees.name
#                     #print birthday_employee
#                     subject = 'BIRTHDAY LIST '
#                     body = 'TODAY IS ** %s ** BIRTHDAY!' % birthday_employee
#                     from_email = 'raveena@5gindia.net'
#                     recipients = [r.strip() for r in mail_list]
#                     send_mail(subject, body, from_email, recipients, fail_silently=False)
