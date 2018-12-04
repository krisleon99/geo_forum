
from django.forms import ModelForm
from .models import Agreeement
from django import forms

class AgreementsForm(ModelForm):
    #start_date = forms.DateTimeField(required=False,label='Fecha de inicio',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #end_date = forms.DateTimeField(required=False,label='Fecha Fin',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #duration = forms.DateTimeField(required=False,label='Duracion',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #signature_date = forms.DateTimeField(required=False,label='Fecha de Firma',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    class Meta:
        model = Agreeement
        fields = "__all__"

class AgreementsUpdate(forms.ModelForm):
    #start_date = forms.DateTimeField(required=False,label='Fecha de inicio',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #end_date = forms.DateTimeField(required=False,label='Fecha Fin',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #duration = forms.DateTimeField(required=False,label='Duracion',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    #signature_date = forms.DateTimeField(required=False,label='Fecha de Firma',widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    class Meta:
        model = Agreeement
        fields = "__all__"
	    #fields = ['prog_number','legasl_instrument', 'document_classification', 'registration_number', 'conterpart_institution_acroniym',
        #  'subscription_field', 'conterpart_sector', 'conterpart_institution','description','signature_date','start_date','end_date','duration','status','modal','version_docto']

class ToDoForm(forms.Form):
    prog_number = forms.CharField(label='Numero de Programa', max_length=100)
    legasl_instrument = forms.CharField(label='Legal', max_length=100)
    document_classification = forms.CharField(label='clasificacion', max_length=100)
    registration_number = forms.CharField(label='registro', max_length=100)
    conterpart_institution_acroniym = forms.CharField(label='institucion', max_length=100)
    subscription_field = forms.CharField(label='campo', max_length=100)
    conterpart_sector = forms.CharField(label='sector', max_length=100)
    conterpart_institution = forms.CharField(label='contraparte', max_length=100)
    description = forms.CharField(label='descripcion', max_length=100)
    #signature_date = forms.DateField(
    #    widget=DateTimePicker(options={"format": "YYYY-MM-DD",
    #                                   "pickTime": False}))
    #duration = forms.DateField(
    #    widget=DateTimePicker(options={"format": "YYYY-MM-DD",
    #                                   "pickTime": False}))
    status = forms.CharField(label='estatus', max_length=100)
    modal = forms.CharField(label='modal', max_length=100)
    version_docto = forms.CharField(label='Version', max_length=100)
    #start_date = forms.DateField(
    #    widget=DateTimePicker(options={"format": "YYYY-MM-DD",
    #                                   "pickTime": False}))
    #end_date = forms.DateTimeField(
     #   required=False,
     #   widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
     #                                  "pickSeconds": False}))
