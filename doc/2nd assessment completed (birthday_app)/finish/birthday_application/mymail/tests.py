from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.core.mail import send_mail
from django.utils import timezone
from django.test import Client 
from .models import Employee
from datetime import date, datetime



class EmployeeRegistrationTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_null_acceptable_for_mail_id(self):
        res = self.client.post('/mymail/add_employee/', {
            'name': 'Raveena',
            'recognition':'Employee',
            'gender':'Female',
            'mail_id':'',
            'date_of_birth':'2018-04-17'
            })
        self.assertEqual(res.status_code, 500)


class EmployeeModelTest(TestCase):

    def test_string_representation(self):
        employee = Employee(name="employee name")
        self.assertEqual(str(employee), employee.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Employee._meta.verbose_name_plural), "employees")

    
class EmployeeListNoneEmpty(TestCase):

    def test_initial_database_is_empty(self):
        """Test if the initial database is empty"""
        list_employees = Employee.objects.all()
        self.assertFalse(list_employees)

class TestViewEmployee(TestCase):

    def test_employee_date_of_birth(self):
        """employee_date_of_birth are correctly identified"""
        employee = Employee.objects.create(name="Raveenapriya", designation="Employee", gender="Female", mail_id="raveena@5gindia.net", date_of_birth="2018-4-17")
        self.assertEqual(employee.date_of_birth, "2018-4-17")
        self.assertNotEqual(employee.date_of_birth, "2017-6-21")


    def test_employee_mail_id(self):
        """employee_mail_id are correctly identified"""
        #employee = Employee.objects.get(name="Nithya")
        employee = Employee.objects.create(name="Nithya", designation="Employee", gender="Female", mail_id="nithya@5gindia.net", date_of_birth="2018-3-19")
        self.assertTrue(employee.name, employee.designation) 
        

class TemplateTest(TestCase):

    def test_template(self):
        self.assertTemplateUsed('birthday_list.html')
        self.assertTemplateUsed(template_name='birthday_list.html')
        self.assertTemplateUsed('administerdetail.html')
        self.assertTemplateUsed('get.html.html')
        self.assertTemplateUsed('index.html')
        self.assertTemplateNotUsed('view_employees.py')


class EmployeeEmailTest(TestCase):

    def test_send_email(self):        

        number_of_emails_sent = send_mail('subject', 
                                          'message', 
                                          'from@example.com',
                                          ['to@example.com'], 
                                          fail_silently=False)        
        self.assertEqual(number_of_emails_sent, 1)
        mail.outbox = []












# class ProjectTests(TestCase):

#     def test_homepage(self):
#         response = self.employee.get('/mymail')
#         self.assertEqual(response.status_code, 200)

    

    # def test_no_employees(self):
    #     Employee.objects.create(name="Raveenapriya")
    #     Employee.objects.create(name="Nithya")
    #     self.assertNumQueries(2)



# class EmployeeTest(TestCase):

#     def create_Employee(self, name="Raveenapriya", recognition="employee", gender="Female", mail_id="Raveena@5gindia.net" ):
#         return Employee.objects.create(name = name, recognition = recognition, gender = gender, mail_id = mail_id)

#     def test_Employee_creation(self):
#         w = self.create_Employee()
#         self.assertTrue(isinstance(w, Employee))
#         self.assertEqual(w.__unicode__(), w.name)







    # def test_one_entry(self):
    #     Employee.objects.create(name ="employee name", recognition = "employee recognition", gender = "employee gender", mail_id = "employee mail_id", date_of_birth = "employee date_of_birth", create_date = "employee create_date")       
    #     self.assertContains(response, '1-name')
    #     self.assertContains(response, '1-recognition')
    #     self.assertContains(response, '1-gender')
    #     self.assertContains(response, '1-mail_id')
    #     self.assertContains(response, '1-date_of_birth')
    #     self.assertContains(response, '1-create_date')



# class ProjectTests(TestCase):

#     def test_homepage(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)








