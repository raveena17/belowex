

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import UserForm, EmployeeForm
from .models import Employee
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
import datetime

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# Data base required quries
class QuerySet:
    today = datetime.date.today()

    # Fetch the who are celebrating their birhday today
    def today_celeb_name_list(self):
        emp_name = Employee.objects.filter(emp_date_of_birth__month=self.today.month).filter(emp_date_of_birth__day=self.today.day).values_list('emp_name', flat=True)
        name_list = [str(name) for name in emp_name]
        return name_list

    # Fetch all employees email list
    def all_employee_email_list(self):
        emp_mail = Employee.objects.values_list('emp_email', flat=True).distinct()
        mail_list = [str(mail) for mail in emp_mail]
        return mail_list

    # Filtered current month celebration list using system date
    def current_month_wish_list(self):
        current_month_birthday_list = Employee.objects.filter(emp_date_of_birth__month=self.today.month).order_by('emp_date_of_birth')
        return current_month_birthday_list

    # Filterd data by feild id
    def filter_data_by_field_id(self, field_id):
        filterd_data_by_field_id = Employee.objects.get(pk=field_id)
        return filterd_data_by_field_id


# Redirect to my home page if user signed sucessfully
def index(request):
    if request.user.is_authenticated():
        username = request.user
        return render(request, 'home.html', {'username': username})
    else:
        return render(request, 'login.html')


# Create a new user
def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                username = request.user
                return render(request, 'home.html', {'username': username})
    return render(request, 'register.html', {'form': form})


# Sign in an exixting user
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {'username': username})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


# Signed out and redirect to login page
def signout(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'login.html', {'form': form})


# Redirect the page to wish list with logined username
def wish_list(request):
    username = request.user
    return render(request, 'wish_list.html', {'username': username})


# Add an employee as new entry
def add_employee(request):
    username = request.user
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.emp_name = request.POST['emp_name']
            employee.emp_gender = request.POST['emp_gender']
            employee.emp_date_of_birth = request.POST['emp_date_of_birth']
            employee.emp_email = request.POST['emp_email']
            employee.emp_contact_number = request.POST['emp_contact_number']
            employee.emp_address_line_1 = request.POST['emp_address_line_1']
            employee.emp_address_line_2 = request.POST['emp_address_line_2']
            employee.emp_address_city = request.POST['emp_address_city']
            employee.emp_address_state = request.POST['emp_address_state']
            employee.emp_address_country = request.POST['emp_address_country']
            employee.emp_photo = request.FILES['emp_photo']
            file_type = employee.emp_photo.url.split('.')[-1]
            file_type = file_type.lower()

            # Check the uploded file image format or not
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'username': username,
                    'employee': employee,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'add_employee.html', context)
            employee.save()
            context = {
                    'username': username,
                    'employee': employee,
            }
            return render(request, 'wish_list.html', context)
    context = {
        'form': form,
        'username': username,
    }
    return render(request, 'add_employee.html', context)


# Update an employee detail
def update_employee(request, field_id):
    queryset = QuerySet()
    employee = queryset.filter_data_by_field_id(field_id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
    username = request.user
    if request.POST:
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'username': username,
            }
            return render(request, 'wish_list.html', context)
        else:
            context = {
                'form': form,
                'username': username,
            }
            return render(request, 'edit_employee.html', context)
    context = {
        'form': form,
        'username': username,
    }
    return render(request, 'edit_employee.html', context)


# Delete an employee with their unique field_id
def delete_employee(request, field_id):
    queryset = QuerySet()
    employee = queryset.filter_data_by_field_id(field_id)
    employee.delete()
    latest_birthdays = queryset.current_month_wish_list()
    username = request.user
    context = {
        'username': username,
        'latest_birthdays': latest_birthdays,
    }
    return render(request, 'employee_list.html', context)


# Current month birthday celebation list are displayed on a template as view
class EmployeeView(TemplateView):
    template_name = "employee_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeView, self).get_context_data(**kwargs)
        queryset = QuerySet()
        latest_birthdays = queryset.current_month_wish_list()
        context = {

            'latest_birthdays': latest_birthdays,
        }
        return context


'''Wishes mail send to employess
   automatically triggered by cron
   if date_of_celebration today'''


# Get birthday details from DB according to current date
def get_wishes(request):
    queryset = QuerySet()
    name = queryset.today_celeb_name_list()
    mail = queryset.all_employee_email_list()
    message_content(name, mail)


# Generate message content with thier details
def message_content(name, mail):
    for index in range(len(name)):
        subject = 'Its Birthday Time For %s' % name[index]
        message = 'Our colleague %s' % name[index]
        to_mail = mail
        send_email(subject, message, to_mail)


# Send mail to all employee
def send_email(subject, message, to_mail):
    email = EmailMessage(subject, message, to=to_mail)
    status = email.send()
    return status

-- 

Regards,

Arun Selvakumar G

Fifth Generation Technologies India Pvt Ltd.
TS 140, Block 2 & 9, Fourth Floor
Elnet Software City
Rajiv Gandhi Salai
Taramani, Chennai 600 113.
Landline: +91-44-2254 1771 / 72 / 73
Cell No:9944845547

*** DISCLAIMER ***This e-mail and any files transmitted with it are for the sole use of the intended recipient(s) and may contain confidential and privileged information. If you are not the intended recipient, please contact the sender by reply e-mail and destroy all copies of the original message and attachments. E-mail transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability for any errors or omissions in the contents of this message, which arise as a result of e-mail transmission. The views expressed in this E-mail message (including the enclosure/(s) or attachment/(s) if any) are those of the individual sender, except where the sender expressly, and with authority, states them to be the views of the company.
