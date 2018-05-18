from django.conf.urls import url
from .import views

app_name = 'mymail'
urlpatterns = [
	#url(r'^birthdaylist/$', views.find_birthday, name='find_birthday'),
	
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^employee/entry/$',views.EmployeeEntry.as_view(),name='employee-entry'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeUpdate.as_view(), name='employee-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.EmployeeDelete.as_view(), name='employee-delete'),
 
	#url(r'^getdata/', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
  
    #url(r'^templates/$', views.index),
    
]