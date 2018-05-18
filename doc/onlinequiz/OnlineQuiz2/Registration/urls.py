from django.conf.urls import url
from .import views

app_name = 'Registration'
urlpatterns = [
	url(r'^$', views.view_homepage, name='view_homepage'),
	url(r'^attendee_register/$', views.attendee_register, name='attendee_register'),
	url(r'^add_attendee/$', views.add_attendee, name='add_attendee'),
	url(r'^questions/$', views.IndexView.as_view(), name='index'),
	url(r'^questions/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	]