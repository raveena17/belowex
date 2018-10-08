# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

"""
    Leave Admin
"""

from project_management.users.models import *
from project_management.leave.models import *


class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'request_id',
        'request_date',
        'empid',
        'leave_from',
        'leave_to',
        'no_of_days',
        'leave_nature',
        'approved_by',
        'approval_status')


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'empid',
        'cur_year',
        'leave_id',
        'total_leave',
        'balance_leave')


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'leave_id',
        'leave_type',
        'no_of_days',
        'current_year',
        'leave_status',
        'organization')


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'request_id',
        'leave_date',
        'request_date',
        'empid',
        'leave_reason',
        'approved_by',
        'no_of_hours',
        'approval_status',
        'reject_reason')


admin.site.register(LeaveRequest)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(ShortLeaveRequest)
