from django.conf.urls import url
from .import views

app_name = 'Registration'
urlpatterns = [
	url(r'^$', views.view_homepage, name='view_homepage'),
	url(r'^get_value/$', views.get_value, name='get_value'),
	url(r'^add_attendee_detail/$', views.add_attendee_detail, name='add_attendee_detail'),
]