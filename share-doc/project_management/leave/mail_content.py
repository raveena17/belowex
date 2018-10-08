# from .models import *
# from .forms import *
# from .views import *
# from django.views.decorators.http import require_http_methods
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage, EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context



# def make_mail_content(user,select_leave,from_date,to_date, no_of_days,reason,datas, approver):
#         import pdb;pdb.set_trace()

#         # list = UserProfile.objects.filter(user=empid, user__is_active=True)

#         now = datetime.datetime.now()
#         user = user
#         sender = user.email
#         recipient = [approver.email]
#         template_name = 'Leave_Reminder.html'
#         subject = user.first_name+' '+ 'has applied leave'
#         content = make_html_content(template_name, {
#             'reporting_senior': approver,
#             'type':select_leave, 
#             'from_date':from_date,
#             'to_date':to_date,
#             'count':no_of_days,
#             'reason':reason,
#             'datas':datas, 
#             'user':user, 
#             'now': now})
#         message = send_mail_for_alert(content, subject, sender, recipient)

# def make_html_content(template_name, context):
#     template = get_template(template_name)
#     html_content = template.render(context)
#     return html_content

# def send_mail_for_alert(html_content, subject, sender, recipient):
#         msg = EmailMultiAlternatives(subject, html_content, sender, recipient)
#         msg.attach_alternative(html_content, "text/html")
#         status = msg.send()
#         return status