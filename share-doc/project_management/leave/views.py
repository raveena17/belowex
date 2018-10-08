from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.template import RequestContext
from project_management.leave.models import *
from project_management.leave.forms import *
from django.views.generic import RedirectView
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from project_management.users.models import *
from django.contrib.auth.models import User, Group
from datetime import date, timedelta
from project_management.alert.models import *
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.response import TemplateResponse
from django.db.models import Sum

class SubListView(ListView):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(SubListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

@require_http_methods(["GET"])
def get_holiday(request):
    today = datetime.date.today()
    holydays = Holiday.objects.filter(
        holdate__year=today.year).values_list('holdate')
    return JsonResponse(list(holydays), safe=False)

@require_http_methods(["GET"])
def get_leave_status(request):
    listdata = get_current_status_for_user(request)
    response = render_to_template(
                            listdata, request
                        )
    return JsonResponse(response, safe=False)

def render_to_template(listdata, request):
        template = TemplateResponse(request, 'leave_table.html', {
        'datas': listdata
        })
        template.render()
        return template.content

@login_required
def leave_list(request):
    Leave_list = LeaveRequest.objects.filter(empid=request.user)
    data_set = get_current_status_for_user(request)
    
    return render(request, 'Leave_list.html', {
                  'Leave_list': Leave_list, 'data_set': data_set})

def get_current_status_for_user(request):
    today = datetime.date.today()
    list_data=[]
    status_list = Status.objects.filter(empid=request.user, cur_year=today.year)
    for status in status_list:
        _type = Type.objects.get(current_year=today.year, leave_id=status.leave_id)
        leave = LeaveRequest.objects.filter(
            leave_nature__leave_id=status.leave_id,
            empid=request.user,
            request_date__year=today.year,
            approval_status="Not Yet Approved"
        )
        if leave:
            no_of_days = leave.aggregate(Sum('no_of_days'))['no_of_days__sum']
            list_data.append({
                'leave_type': _type.leave_type,
                'current_balence': status.balance_leave,
                'appied_for': no_of_days,
                'balence_after_approval': status.balance_leave-no_of_days,
            })
        else:
            balance = 0
            list_data.append({
                'leave_type': _type.leave_type,
                'current_balence': status.balance_leave,
                'appied_for': balance,
                'balence_after_approval': balance
            })
    return list_data


@login_required
def manage_leave(request, id=None, RedirectView=leave_list):
    leave = None
    if id:
        leave = get_object_or_404(LeaveRequest, pk=id)
    today = datetime.date.today()
    holydays = Holiday.objects.filter(holdate__year=today.year)
    datas = []
    if request.method == 'POST':
        LeaveForm = LeaveReportForm(request.user, request.POST, instance=leave)
        if LeaveForm.is_valid():
            leave_form = LeaveForm.save(commit=False)

            leave_form.request_date = datetime.date.today()
            approver = leave_form.approved_by
            from_date = leave_form.leave_from
            to_date = leave_form.leave_to
            reason = leave_form.leave_reason
            no_of_days = leave_form.no_of_days

            user_status_list = Status.objects.filter(
                empid=request.user.username, cur_year=today.year)
            '''Get leave_id for employee selected leave type'''
            for status in user_status_list:
                _type = Type.objects.get(current_year=today.year, leave_id=status.leave_id)
                select_leave = leave_form.leave_nature
                balance = 0
                datas.append({
                    'leave_type': _type.leave_type,
                    'current_balence': status.balance_leave,
                    'appied_for': balance,
                    'balence_after_approval': balance,
                    'lop':balance

                })

                if select_leave.leave_type == 'LOP':
                        leave_form.lop = no_of_days

                if select_leave==_type:
                    import pdb;pdb.set_trace()
                    if status.balance_leave<no_of_days:
                        lop = status.balance_leave-no_of_days
                        leave_form.lop = lop

                    datas.append({
                        'leave_type': _type.leave_type,
                        'current_balence': status.balance_leave,
                        'appied_for': no_of_days,
                        'balence_after_approval': status.balance_leave-no_of_days,
                        'lop': int(lop)
                    })


                for data in datas:
                    if data['leave_type'] == select_leave.leave_type and data['appied_for']==0:
                        remove_data = datas.remove(data)

            leave_form.save()
            make_mail_content(
                request,select_leave,from_date,to_date,no_of_days,reason,datas,approver)
            messages.success(request, _('Leave created Sucessfully'))
        return HttpResponseRedirect(reverse(RedirectView))
    else:
        LeaveForm = LeaveReportForm(request.user, instance=leave)
    return render(request, 'Leave_form.html', {
                  'form': LeaveForm, 'holydays': holydays})


@login_required
def manage_shortleave(request, id=None, RedirectView=leave_list):
    shortleave = None
    if id:
        shortleave = get_object_or_404(LeaveRequest, pk=id)
    today = datetime.date.today()
    holydays = Holiday.objects.filter(holdate__year=today.year)
    if request.method == 'POST':
        ShortLeaveForm = ShortLeaveRequestForm(request.user, request.POST)
        if ShortLeaveForm.is_valid():
            shortleave_form = ShortLeaveForm.save(commit=False)
            shortleave_form.request_date = datetime.date.today()
            shortleave_form.save()
            messages.success(request, _('ShortLeave created Sucessfully'))
        return HttpResponseRedirect(reverse(RedirectView))
    else:
        ShortLeaveForm = ShortLeaveRequestForm(request.user)
    return render(request, 'Leave_form.html', {
                  'short_leave_form': ShortLeaveForm, 'holydays': holydays})


def make_mail_content(request, select_leave, from_date,
                      to_date, no_of_days, reason, datas, approver):
    now = datetime.datetime.now()
    user = request.user
    sender = user.email
    recipient = [approver.email]
    template_name = 'Leave_Reminder.html'
    subject = user.first_name + ' ' + 'has applied leave'
    content = make_html_content(template_name, {
        'reporting_senior': approver.first_name,
        'from_date': from_date,
        'type': select_leave,
        'to_date': to_date,
        'no_of_days': no_of_days,
        'reason': reason,
        'datas': datas,
        'user': user.first_name,
        'now': now})
    message = send_mail_for_alert(content, subject, sender, recipient)


def make_html_content(template_name, context):
    template = get_template(template_name)
    html_content = template.render(context)
    return html_content


def send_mail_for_alert(html_content, subject, sender, recipient):
    msg = EmailMultiAlternatives(subject, html_content, sender, recipient)
    msg.attach_alternative(html_content, "text/html")
    status = msg.send()
    return status


@login_required
def delete_leave(request):
    if request.method == 'POST':
        leave_ids = request.POST.getlist('leave_pk')
        LeaveRequest.objects.filter(pk__in=leave_ids).delete()
        messages.success(request, _('Leave deleted sucessfully'))
    return HttpResponseRedirect(reverse(leave_list))



































# @login_required
# def manage_leave(request, id=None, RedirectView=leave_list):
#     leave = None
#     if id:
#         leave = get_object_or_404(LeaveRequest, pk=id)
#     today = datetime.date.today()
#     holydays = Holiday.objects.filter(holdate__year=today.year)
#     datas = []
#     if request.method == 'POST':
#         # request_copy = request.POST.copy()
#         # l_form = SettingsForm(request_copy)
#         LeaveForm = LeaveReportForm(request.user, request.POST, instance=leave)
#         if LeaveForm.is_valid():
#             leave_form = LeaveForm.save(commit=False)
#             approver = leave_form.approved_by
#             from_date = leave_form.leave_from
#             to_date = leave_form.leave_to
#             reason = leave_form.leave_reason

#             leave_form.request_date = datetime.date.today()
#             no_of_days = leave_form.no_of_days
#             user_list = Status.objects.filter(
#                 empid=request.user.username, cur_year=today.year)
#             '''Get leave_id for employee selected leave type'''
#             select_leave = leave_form.leave_nature

#             leave_type = Type.objects.filter(current_year=today.year)
#             for leave in leave_type:
#                 if select_leave == leave:
#                     selected_leaveid = leave.leave_id
#                     for user in user_list:
#                         if leave.leave_type == 'LOP':
#                             leave_form.lop = no_of_days

#                         status_leaveid = user.leave_id
#                         balance_leave = user.balance_leave
#                         total_leave = user.total_leave
#                         if selected_leaveid == status_leaveid:
#                             '''Reduce the leave for employee status in Status table- after approval'''
#                             leave_count = balance_leave - no_of_days
#                             if leave_form.approval_status == "Approved":
#                                 emp_balance_leave = Status.object.get(
#                                     empid=request.user)
#                                 emp_balance_leave.balance_leave = leave_count
#                                 emp_balance_leave.save()
#                             dict_value = {
#                                 'leave_type': leave.leave_type,
#                                 'current_balence': balance_leave,
#                                 'appied_for': no_of_days,
#                                 'balence_after_approval': balance_leave - no_of_days
#                             }
#                             datas.append(dict_value)

#                         else:
#                             typ = Type.objects.filter(
#                                 current_year=today.year, leave_id=status_leaveid)
#                             balance = '0'
#                             bal = user.balance_leave
#                             dict_value = {
#                                 'leave_type': str(typ[0]),
#                                 'current_balence': user.balance_leave,
#                                 'appied_for': balance,
#                                 'balence_after_approval': balance
#                             }
#                             datas.append(dict_value)

#             # import pdb;pdb.set_trace()
#             leave_form.save()

#             make_mail_content(
#                 request,select_leave,from_date,to_date,no_of_days,reason,datas,approver)
#             messages.success(request, _('Leave created Sucessfully'))
#         return HttpResponseRedirect(reverse(RedirectView))
#     else:
#         LeaveForm = LeaveReportForm(request.user, instance=leave)
#         # l_form = SettingsForm()

#     return render(request, 'Leave_form.html', {
#                   'form': LeaveForm, 'holydays': holydays})
#     # 'form': LeaveForm, 'holydays': holydays, "l_form":l_form})