"""
    Url for business unit application
"""

# from django.conf.urls.defaults import patterns
from django.conf.urls import include, url
# from project_management.leave import views as leave_views
from project_management.leave.views import *


urlpatterns = [
    url(r'^create/$', manage_leave),
    url(r'^short/create/$', manage_shortleave),
    url(r'^update/(?P<id>\d+)/$', manage_leave),
    url(r'^list/$', leave_list),
    url(r'^delete/$', delete_leave),
    # url(r'^cur_status/$', get_applied_record_for_user),
    url(r'^holiday/$', get_holiday),
    url(r'^status/$', get_leave_status),

]
