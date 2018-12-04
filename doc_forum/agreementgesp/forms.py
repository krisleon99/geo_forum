from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm
from .models import Agreementgs, Conacyt_fund, PeopleContac, Accomplishment
from django import forms

from crispy_forms.helper import FormHelper


#start_date = forms.DateTimeField(required=False,label='Fecha de inicio',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #end_date = forms.DateTimeField(required=False,label='Fecha Fin',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))

class AgreementsForm(ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['setid', 'unity_name', 'ambit', 'objective', 'institution', 'start_date', 'end_date', 'technical_support', 'comments']


class AgreementsEspForm(ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['setid', 'unity_name', 'ambit', 'project_type', 'project_name', 'project_key', 'objective', 'conacyt_fund', 'other_financing', 'project_type_2', 'start_date', 'end_date', 'technical_support', 'project_completed', 'comments']


class AgreementsUpdate(forms.ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['setid', 'unity_name', 'ambit', 'objective', 'institution', 'start_date', 'end_date', 'technical_support', 'comments']


class AgreementsEspUpdate(forms.ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['setid', 'unity_name', 'ambit', 'project_type', 'project_name', 'project_key', 'objective', 'conacyt_fund', 'other_financing', 'project_type_2', 'start_date', 'end_date', 'technical_support', 'project_completed', 'comments']


class AgreementsEspResourcese(forms.ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['resources', 'authorized_amount', 'authorized_implemented']


class AgreementsProgressForm(ModelForm):
    class Meta:
        model = Agreementgs
        fields = ['progress']


class Conacyt_fundForm(ModelForm):
    class Meta:
        model = Conacyt_fund
        fields = "__all__"


class Conacyt_fundUpdate(forms.ModelForm):
    class Meta:
        model = Conacyt_fund
        fields = "__all__"


class PeopleContacForm(ModelForm):
    class Meta:
        model = PeopleContac
        fields = "__all__"


class PeopleContacUpdate(forms.ModelForm):
    class Meta:
        model = PeopleContac
        fields = "__all__"


class AccomplishmentForm(ModelForm):
    class Meta:
        model = Accomplishment
        fields = "__all__"


class AccomplishmentUpdate(forms.ModelForm):
    class Meta:
        model = Accomplishment
        fields = "__all__"

class Add_Accomplishment(forms.ModelForm):
	class Meta:
		model = Accomplishment
		fields = ['description']