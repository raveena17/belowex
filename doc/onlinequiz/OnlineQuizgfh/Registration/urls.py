from django.conf.urls import url
from .import views

app_name = 'Registration'
urlpatterns = [
	
	url(r'^$', views.view_homepage, name='view_homepage'),
	url(r'^attendee_register/$', views.attendee_register, name='attendee_register'),
	url(r'^add_attendee/$', views.add_attendee, name='add_attendee'),
	url(r'^question/$', views.IndexView.as_view(), name='index'),

	url(r'^question/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),




	url(r'^language/$', views.view_language, name='view_language'),
# url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

	# url(r'^(?P<question_id>[0-9]+)/count/$', views.count, name='count'),

	url(r'^(?P<question_id>[0-9]+)/next/$', views.get_next_id, name='next'),
	url(r'^(?P<question_id>[0-9]+)/previous/$', views.get_prev_id, name='previous'),











































	# url(r'^$', views.view_homepage, name='view_homepage'),
	# url(r'^attendee_register/$', views.attendee_register, name='attendee_register'),
	# url(r'^add_attendee/$', views.add_attendee, name='add_attendee'),
	# url(r'^questions/$', views.IndexView.as_view(), name='index'),
	# url(r'^questions/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	]