from django.conf.urls import url
from .import views

app_name = 'mymail'
urlpatterns = [
	url(r'^$', views.view_admindetail, name='view_admindetail'),
	url(r'^get_value/$', views.get_value, name='get_value'),
	url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
	url(r'^add_employee/$', views.add_employee, name='add_employee'),
    #url(r'^add_employee/logout/$', views.logout, name='logout'),
    url(r'^birthdaylist/$', views.find_birthday, name='find_birthday'),
	
]
	
	