from django.conf.urls import url
from .import views

app_name = 'mymail'
urlpatterns = [
	url(r'^$', views.view_home, name='view_home'),
	url(r'^employee_list/$', views.view_employee_list, name='view_employee_list'),
	url(r'^employee_register/$', views.employee_register, name='employee_register'),
	url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
	url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
	url(r'^add_employee/$', views.add_employee, name='add_employee'),
    url(r'^birthdaylist/$', views.find_birthday, name='find_birthday'),
    #url(r'^add_employee/logout/$', views.logout, name='logout'),
	
]
	
	