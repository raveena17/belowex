from django.conf.urls import url
from .import views

app_name = 'birthday'
urlpatterns = [
    url(r'^$', views.view_homepage, name='view_homepage'),
    url(r'^employee_list/$',
        views.view_employee_list,
        name='view_employee_list'),
    url(r'^employee_register/$',
        views.employee_register,
        name='employee_register'),
    url(r'^delete_employee/$', views.delete_employee, name='delete_employee'),
    #url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^add_employee/$', views.add_employee, name='add_employee'),
    url(r'^birthday_list/$',
        views.get_employee_by_birthday,
        name='get_employee_by_birthday'),

]
