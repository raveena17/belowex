


forms.py

from django import forms
from .models import Reimbursement, Type, User, Allowance,ReimbursementType, Status
from project_management.users.models import UserProfile
from project_management.client_visit_report.models import ClientVisitReport
from django.forms import widgets, BaseInlineFormSet
from django.forms.models import inlineformset_factory

DATE_INPUT_FORMAT = '%m-%d-%Y'
DATE_FIELD_ATTR = {'class': 'vDateField'}


class ReimbursementModelForm(forms.ModelForm):

	# reporting_seniors = User.objects.filter(
    #     groups__name='Manager', is_active=True)
	# approver = forms.ModelChoiceField(queryset=reporting_seniors)
	status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
	bill_location = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	type = forms.ModelChoiceField(queryset=Type.objects.all(), initial=Type.objects.get(id=1))
	client_visit_report = forms.CharField(widget=forms.HiddenInput(), label='', required=False)

	def __init__(self,user, *args, **kwargs):
		row = kwargs.pop('row')

		super(ReimbursementModelForm, self).__init__(*args, **kwargs)

		self.fields['approver'].queryset = User.objects.filter(groups__name='Manager', is_active=True).exclude(username=user.username)
		
		self.fields['total_amount'].widget.attrs['readonly'] = 'readonly'
		
		self.fields['status'].empty_label = None
		
		self.fields['bill_location'].required = False
		self.fields['notes'].required = False
		# self.initial['status'] = Status.objects.get(status='Pending')
		# self.fields['status'].initial = Status.objects.get(status='Pending')
		if not self.instance.id:
			self.initial['status'] = Status.objects.get(status='Pending').id
			if row == None:
				reporting_senior_name = UserProfile.objects.get(user=user).reporting_senior_name
				self.initial['approver'] = reporting_senior_name.id
				self.initial['type'] = Type.objects.get(id=1)
			else:
				self.initial['type'] = Type.objects.get(id=1)
		else:
			self.make_noneditable(self.instance.id, user)
		

	def make_noneditable(self, instance, user):

		# import pdb;pdb.set_trace()

		reimbursement = Reimbursement.objects.get(id=instance)
		if reimbursement.name == user:
			if reimbursement.status.status == 'Pending':
				self.fields['status'].disabled = True
			else:
				self.fields['name'].disabled = True
				self.fields['approver'].disabled = True
				self.fields['status'].disabled = True
				self.fields['type'].disabled = True
				self.fields['notes'].disabled = True
		else:
			self.fields['name'].disabled = True
			self.fields['approver'].disabled = True
			self.fields['status'].disabled = True
			self.fields['type'].disabled = True
			self.fields['notes'].disabled = True
		# else:
		# 	print "asdasd"
			# self.fields['name'].disabled = True
			# self.fields['approver'].disabled = True
			# self.fields['status'].disabled = True
			# self.fields['type'].disabled = True

	class Meta:

		model = Reimbursement
		exclude = ('created_on', 'details')
		widgets = {
	        'notes':forms.Textarea(attrs={'rows':4, 'cols':24}),
	        'total_amount':forms.NumberInput(attrs={'placeholder':0}),
	        'bill_location':forms.FileInput(attrs={'required':False}),
	        # 'client_visit_report':forms.HiddenInput(attrs={'required':False}),
	        }  



class Reimbursement_form(forms.Form):

	report = forms.ModelChoiceField(queryset=ClientVisitReport.objects.none(), required=False)

	def __init__(self, *args, **kwargs):
		
		super(Reimbursement_form, self).__init__(*args, **kwargs)
		# if self.instance.id:
		# 	print "sadasd", 
			# reimbursement = Reimbursement.objects.get(id=self.instance.id)
			# if reimbursement.name == user:
			# 	if reimbursement.status.status == 'Pending':
			# 		self.fields['report'].disabled = False
			# 	else:
			# 		self.fields['report'].disabled = True
			# else:
			# 	self.fields['report'].disabled = True
		# import pdb;pdb.set_trace()
		# if type:
		# 	type = Type.objects.get(id=1).type
		# 	if type == 'Travel':
		# 		self.fields['report'].queryset = ClientVisitReport.objects.all()
		# 	else:
		# 		self.fields['report'].queryset = Type.objects.all()

class ClientVisitReport_Form(forms.Form):

	prepared_by = forms.CharField(required=False)
	client_name = forms.CharField(required=False)
	visit_location = forms.CharField(required=False)
	from_date = forms.CharField(required=False)
	to_date = forms.CharField(required=False)
	status = forms.CharField(required=False)

	def __init__(self, *args, **kwargs):

		super(ClientVisitReport_Form, self).__init__(*args, **kwargs)
		self.fields['prepared_by'].widget.attrs['readonly'] = 'readonly'
		self.fields['client_name'].widget.attrs['readonly'] = 'readonly'
		self.fields['visit_location'].widget.attrs['readonly'] = 'readonly'
		self.fields['from_date'].widget.attrs['readonly'] = 'readonly'
		self.fields['to_date'].widget.attrs['readonly'] = 'readonly'
		self.fields['status'].widget.attrs['readonly'] = 'readonly'
		self.fields['status'].widget.attrs['class'] = 'status'
		self.fields['status'].widget.attrs['id'] = 'cvr_status'

class AllowanceForm(forms.ModelForm):

    reimbursement = forms.ModelChoiceField(queryset=ReimbursementType.objects.all())
    # budget = forms.NumberInput(attrs={'disabled':True})
    # reimbursement_type = forms.ModelChoiceField(queryset=ReimbursementType.objects.all(), initial=0)

    class Meta:
        model = Allowance
        fields = "__all__"
        widgets = {
            'date' : forms.TextInput(attrs={'class':'datepicker'}),
            'expenditure':forms.NumberInput(attrs={'class': 'expenditure', 'rows':3, 'cols':25}),
            'description':forms.Textarea(attrs={'rows':1, 'cols':25, 'class':'description','required':False}),
            'category':forms.Select(attrs={'class':'category','rows':1, 'cols':10}),
            'budget':forms.NumberInput(attrs={'class':'budget', 'disabled':True, 'required':False}),
            'bill_availability':forms.CheckboxInput(attrs={'class':'bill_availability'}),
            }

class BaseFormSet(BaseInlineFormSet):

    def __init__(self, user, *args, **kwargs):

        super(BaseFormSet, self).__init__(*args, **kwargs)

        if self.instance.id:
            reimbursement = Reimbursement.objects.get(id=self.instance.id)
            if reimbursement.name == user:
                if reimbursement.status.status != 'Pending':
                    self.non_edit()
            else:
            	self.non_edit()
            

    def non_edit(self):
        for form in self.forms:
            form.fields['date'].disabled = True
            form.fields['category'].disabled = True
            form.fields['expenditure'].disabled = True
            form.fields['description'].disabled = True



allowanceInlineFormSet = inlineformset_factory(Reimbursement, Allowance, formset=BaseFormSet, form=AllowanceForm, extra=1)

        


views.py

from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.views.decorators.http import require_http_methods
from project_management.client_visit_report.models import ClientVisitReport
from django.http import JsonResponse
from project_management.reimbursement.models import Status, Type
import datetime
from django.contrib import messages

today = datetime.date.today()

@require_http_methods(["GET"])
def get_type(request):
    # import pdb;pdb.set_trace()
    report = {}
    if request.GET['type'] == 'Travel':
        queryset = ClientVisitReport.objects.all().values('client_name__name', 'id', 'from_date')
        json_type = list(queryset)
    return JsonResponse(json_type, safe=False)

@require_http_methods(["GET"])
def get_report(request):
    # import pdb;pdb.set_trace()
    if request.GET['name'] == 'travel':
        queryset = ClientVisitReport.objects.filter(id=int(request.GET['type'])).values('prepared_by','client_name__name', 'id', 'visit_location','from_date','to_date','is_approved', 'is_rejected')
        json_type = list(queryset)
    return JsonResponse(json_type, safe=False)

def get_user_roles(request):
    groups = request.user.groups.all().values('name')
    user_roles = []
    for index in range(0, (len(groups)-1)):
        role = groups[index].values()[0]
        user_roles.append(role)
    return user_roles


def admin_reimbursement_list(request):
    reimbursements = None
    # import pdb;pdb.set_trace()
    page = request.GET.get('page', 1)

    for role in get_user_roles(request):
        if role == 'Corporate Admin':
            reimbursement = Reimbursement.objects.all()
            reimbursements = paginate_reimbursement(reimbursement, page)
            return render(request, 'reimbursement_records.html',{'reimbursements': reimbursements})

# def add_row(request):
#     import pdb;pdb.set_trace()

#     queryDict = request.POST
#     request_copy['allowance_set-TOTAL_FORMS'] = int(request_copy['allowance_set-TOTAL_FORMS'])+ 1
#     reimbursement_form = ReimbursementModelForm(request.user, request_copy, request.FILES)
#     type_form = Reimbursement_form(request_copy)
#     clientVisitReport_form = ClientVisitReport_Form(request.POST) 

#     formset = allowanceInlineFormSet(request.user, request_copy, instance=reimbursement)
#     reimbursement_form = ReimbursementModelForm(request.user, request_copy, instance=reimbursement)    
#     print "sdhguydsuid"

@csrf_exempt
@login_required
def reimbursement_list(request):
    # import pdb;pdb.set_trace()
    user_reimbursement = None
    requests = None
    page = request.GET.get('page', 1)
    reimbursement = Reimbursement.objects.filter(name=request.user)
    user_reimbursement = paginate_reimbursement(reimbursement, page)
    
    if 'Corporate Admin' not in get_user_roles(request):
        reimbursement = Reimbursement.objects.filter(approver=request.user)
        requests = paginate_reimbursement(reimbursement, page)
    else:
        reimbursements = Reimbursement.objects.filter(approver=request.user)#.exclude(status__status__in=['Approved','Processed'])
        approved_reimbursements = Reimbursement.objects.filter(status__status__in=['Approved','Processed']).exclude(approver=request.user)
        reimbursement = list(chain(reimbursements, approved_reimbursements))
        requests = paginate_reimbursement(reimbursement, page)

            
    return render(request, 'reimbursement_list4.html',
                {'user_reimbursement':user_reimbursement,
                'requests':requests})

def paginate_reimbursement(reimbursement, page):

    
    paginator = Paginator(reimbursement, 10)
    try:
        reimbursements = paginator.page(page)
    except PageNotAnInteger:
        reimbursements = paginator.page(1)
    except EmptyPage:
        reimbursements = paginator.page(paginator.num_pages)
    return reimbursements

# @require_http_methods(["GET"])
# def set_report(request):
# 	# import pdb;pdb.set_trace()
# 	report = {}
# 	type = Type.objects.get(id=int(request.GET['type']))
# 	if type.type == 'Travel':
# 		queryset = ClientVisitReport.objects.all().values('client_name__name', 'id')
# 		json_type = list(queryset)
# 		report['client'] = json_type
# 	return JsonResponse(report, safe=False)


def get_details(request):

        details = {}
        details['preparedBy'] = request.POST['prepared_by']
        details['clientName'] = request.POST['client_name']
        details['visitLocation'] = request.POST['visit_location']
        details['fromDate'] = request.POST['from_date']
        details['toDate'] = request.POST['to_date']
        return details

@csrf_exempt
@login_required
def manage_reimbursement(request, id=None):
    # import pdb;pdb.set_trace()
    row = None
    selectedValue = None

    if id:
        reimbursement = Reimbursement.objects.get(pk=id)  # if this is an edit form, replace the author instance with the existing one
    else: 
        reimbursement = Reimbursement()

    request_copy = request.POST.copy()

    reimbursement_form = ReimbursementModelForm(request.user, instance=reimbursement, row=row) # setup a form for the parent    
    type_form = Reimbursement_form()
    clientVisitReport_form = ClientVisitReport_Form()
    formset = allowanceInlineFormSet(request.user, instance=reimbursement)

    if request.method == 'POST':

        queryDict = request.POST
        
        if 'add-row' in queryDict.keys():
    
            request_copy['allowance_set-TOTAL_FORMS'] = int(request_copy['allowance_set-TOTAL_FORMS'])+ 1
            # formset = allowanceInlineFormSet(request_copy, instance=reimbursement)
            type = Type.objects.get(id=int(request_copy['type']))
            if type.type == 'Travel':
                selectedValue = request_copy['report']
            reimbursement_form = ReimbursementModelForm(request.user, request_copy, request.FILES, row=queryDict['add-row'])
            type_form = Reimbursement_form(request_copy)
            clientVisitReport_form = ClientVisitReport_Form(request.POST)
            formset = allowanceInlineFormSet(request.user, request_copy, request.FILES, instance=reimbursement) 
        else:
        
            request_copy['name'] = request.user.id
            # request_copy['status'] = request.POST.getlist('status')[0]
            request_copy['status'] = Status.objects.get(status='Pending').id
            request_copy['client_visit_report'] = request_copy['report']
            reimbursement_form = ReimbursementModelForm(request.user, request_copy, request.FILES, instance=reimbursement, row=row)
            type_form = Reimbursement_form(request_copy)
            clientVisitReport_form = ClientVisitReport_Form(request.POST) 
            

            if reimbursement_form.is_valid():
                created_reimbursement = reimbursement_form.save(commit=False)
                
                created_reimbursement.created_on = today
                # type = Type.objects.get(id=int(request_copy['type'])).type
                created_reimbursement.details = get_details(request)
                # if type == 'Travel':
                #     created_reimbursement.details = get_details(request)
                #     formset = allowanceInlineFormSet(request.user, request_copy, request.FILES, instance=created_reimbursement)
                # else:
                #     formset = allowanceInlineFormSet(request.user, request_copy, request.FILES, instance=created_reimbursement)
                
                formset = allowanceInlineFormSet(request.user, request_copy, request.FILES, instance=created_reimbursement)
                if formset.is_valid():
                    created_reimbursement.save()
                    formset.save()
                messages.success(request,
                                     ('Reimbursement created Successfully'))
                return HttpResponseRedirect('/reimbursement/list/')

    return render(request, 'reimbursement_form11.html', {'reimbursementModelForm': reimbursement_form, 'type_form':type_form, 'clientVisitReport_form':clientVisitReport_form, 'formset':formset, 'selectedValue':selectedValue})

@csrf_exempt
@login_required
def Approve(request, id=None):
    # import pdb;pdb.set_trace()
    
    reimbursement = Reimbursement.objects.get(pk=id)
    reimbursement.status = Status.objects.get(status='Approved')
    
    reimbursement.save();
    messages.success(request,
                                 ('Reimbursement Approved Successfully'))
    return HttpResponseRedirect('/reimbursement/list/')

@csrf_exempt
@login_required
def Reject(request, id=None):
    # import pdb;pdb.set_trace()
    
    reimbursement = Reimbursement.objects.get(pk=id)
    reimbursement.status = Status.objects.get(status='Rejected')
    reimbursement.save()
    messages.success(request,
                                 ('Reimbursement Rejected Successfully'))
    return HttpResponseRedirect('/reimbursement/list/')

@csrf_exempt
@login_required
def Process(request, id=None):
    # import pdb;pdb.set_trace()
    # files = request.FILES.getlist('bill_location')
    reimbursement = Reimbursement.objects.get(pk=id)
    reimbursement.status = Status.objects.get(status='Processed')
    reimbursement.bill_location = request.FILES.get('bill_location')
    reimbursement.save()
    messages.success(request,
                                 ('Reimbursement Processed Successfully'))
    return HttpResponseRedirect('/reimbursement/list/')

        

