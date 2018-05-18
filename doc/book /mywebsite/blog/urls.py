from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^view_admindetail/$', views.view_admindetail, name='view_admindetail'),
    url(r'^view_userdetail/$', views.view_userdetail, name = 'view_userdetail'),
    #url(r'^get_book/$', views.get_book, name='get_book'),
    url(r'^get_value/$', views.get_value, name='get_value'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^get_comment/(?P<id>[0-9]+)/$', views.get_comment, name='get_comment'),
    url(r'^add_comment/(?P<id>[0-9]+)/$', views.add_comment, name='add_comment'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^add_book/logout/$', views.logout, name='logout'),
    ]