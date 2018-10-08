"""
    Leave Application forms
"""
from django import forms
from project_management.leave.models import *

import datetime


DATE_INPUT_FORMAT = '%m-%d-%Y'
DATE_FIELD_ATTR = {'class': 'vDateField'}


class DateInput(forms.DateInput):

    input_type = 'date'


class LeaveReportForm(forms.ModelForm):
    """
        form which represents the leave_application.
    """

    def __init__(self, user, *args, **kwargs):
        # import pdb;pdb.set_trace()
        super(self.__class__, self).__init__(*args, **kwargs)
        self.initial['empid'] = user
        self.fields['empid'].empty_label = None
        self.fields['empid'].queryset = User.objects.filter(id=user.id)
        #self.fields['empid'].widget.attrs['disabled'] = True
        today = datetime.date.today()

        # self.initial['leave_from'] = today
        # self.initial['leave_to'] = today

        leavenature= Type.objects.filter(current_year=today.year)
        # import pdb;pdb.set_trace()
        self.fields['leave_nature'].queryset = leavenature
        self.fields['leave_nature'].empty_label = None

        reporting_senior_name = UserProfile.objects.get(
            user=user).reporting_senior_name
        self.fields['approved_by'].empty_label = None
        self.fields['approved_by'].queryset = User.objects.filter(id=reporting_senior_name.id)        
        self.initial['approved_by'] = reporting_senior_name.id


    def save(self, commit=True):
        leave = super(LeaveReportForm, self).save(commit=False)

        if commit:
            leave.save()
        return leave

    class Meta:
        model = LeaveRequest
        exclude = (
            'request_id',
            'request_date',
            'approval_status',
            'reject_reason')


class ShortLeaveRequestForm(forms.ModelForm):
    """
        form which represents the leave_application.
    """

    def __init__(self, user, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.initial['empid'] = user
        # self.fields['empid'].disabled = True
        reporting_senior_name = UserProfile.objects.get(
            user=user).reporting_senior_name
        self.initial['approved_by'] = reporting_senior_name.id
        # self.fields['approved_by'].disabled = True

        # repeat = forms.BooleanField(required=False)
        # short = forms.ModelChoiceField(required=False, )

    def save(self, commit=True):
        leave = super(ShortLeaveRequestForm, self).save(commit=False)
        if commit:
            leave.save()
        return leave

    class Meta:
        model = ShortLeaveRequest
        exclude = ('request_id', 'request_date', 'reject_reason', 'approval_status')



class SettingsForm(forms.Form):
    half = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"Leave"}))
    short = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"Leave"}))
