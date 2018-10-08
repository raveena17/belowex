from __future__ import unicode_literals
from django.db import models
import datetime
from project_management.users.models import *
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from client_visit_report.emailmanager import send
from project_management.users.models import *
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from netifaces import interfaces, ifaddresses, AF_INET
from django.core.mail import send_mail
from leave.views import *


class Type(models.Model):

    leave_id = models.AutoField(primary_key=True)
    leave_type = models.CharField(max_length=200, blank=False, null=False)
    no_of_days = models.IntegerField()
    current_year = models.IntegerField()
    leave_status = models.CharField(max_length=200, blank=False, null=False)
    organization = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.leave_type)

    class Meta:
        db_table = 'leave_types'
        verbose_name_plural = "Leave Type"


class LeaveRequest(models.Model):

    request_id = models.AutoField(primary_key=True)
    request_date = models.DateField(null=True, blank=True)
    empid = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_empid",
        verbose_name='empid',
        null=True,
        db_column='empid')
    leave_from = models.DateField(null=True, blank=True)
    leave_to = models.DateField(null=True, blank=True)
    no_of_days = models.IntegerField()
    leave_nature = models.ForeignKey(
        Type,
        related_name="%(app_label)s_%(class)s_leave_nature",
        verbose_name='leave_nature',
        null=True,
        db_column='leave_nature')
    leave_reason = models.TextField(max_length=200, blank=True, null=True)
    approved_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_approved_by",
        verbose_name='approved_by',
        null=True,
        db_column='approved_by')
    approval_status = models.CharField(
        default="Not Yet Approved",
        max_length=200,
        blank=False,
        null=False)
    reject_reason = models.TextField(max_length=200, blank=True, null=True)
    lop = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True)

    def __unicode__(self):
        return str(self.empid)

    class Meta:
        db_table = 'leave_requests'
        verbose_name_plural = "Leave Request "


class Status(models.Model):

    id = models.AutoField(primary_key=True)
    empid = models.CharField(max_length=200, blank=False, null=False)
    cur_year = models.IntegerField()
    leave_id = models.IntegerField()
    total_leave = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    balance_leave = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.empid)

    class Meta:
        db_table = 'leave_statuses'
        verbose_name_plural = "Leave Status"


class ShortLeaveRequest(models.Model):

    request_id = models.AutoField(primary_key=True)
    leave_date = models.DateField(null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    empid = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_employee",
        verbose_name='employee',
        null=True,
        db_column='empid')
    leave_reason = models.TextField(max_length=200, blank=True, null=True)
    approved_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_manager",
        verbose_name='manager',
        null=True,
        db_column='approved_by')
    no_of_hours = models.IntegerField(default=1)
    approval_status = models.CharField(max_length=200, blank=False, null=False)
    reject_reason = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return str(self.empid)

    class Meta:
        db_table = 'shortleave_requests'
        verbose_name_plural = "Short Leave Request "


# def send_leavereport_mail(sender, instance=None,
#                         created=False, update_fields=None, **kwargs):
# 	print "hi"
    # if update_fields:
    # make_mail_content(request, datas, approver)
    # else:
    # 	make_mail_content(request, datas, approver)
    #     if 'is_approved' or 'is_rejected' in update_fields:
    #         pass
    # else:

# def send_leavereport_mail(sender, instance=None, created=False, update_fields=None, **kwargs):
    # address = [i['addr'] for i in ifaddresses(
    #     'enp4s0').setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    # #production -  address = [i['addr'] for i in ifaddresses('eth0').setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    # recipient = instance.approved_by
    # sender = instance.empid
    # subject = "Approve Leave Form"
    # template = get_template('leave_approval.txt')
    # text_body = template.render({
    #     'leave': instance,
    #     'recipient': recipient,
    #     'reporting_senior_name': instance.approved_by.first_name,
    #     # 'full_domain': "http://" + address[0] + ":9073/login/",
    #     'full_domain': "http://" + address[0] + ":8000/login/",
    #     'request_user': instance.empid
    # })
    # status = send(recipient, sender, subject, text_body)

# models.signals.post_save.connect(send_leavereport_mail, sender=LeaveRequest)
# models.signals.post_save.connect(send_leavereport_mail, sender=ShortLeaveRequest)


# class Credit(models.Model):

# 	empid = models.ForeignKey(User, verbose_name=('user'),
#                              related_name="%(app_label)s_%(class)s_user")
# 	# leave_id = models.IntegerField(unique=True)
# 	leave_id = models.IntegerField()
# 	no_of_days = models.IntegerField()
# 	credit_date = models.DateField(null=True, blank=True)
# 	cur_year = models.IntegerField()

# 	def __str__(self):
# 		return str(self.empid)

# class Detail(models.Model):

# 	request_id =
# 	leave_date = models.DateField(null=True, blank=True)
# 	isfull = models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.empid)
