from django.forms import ModelForm
from .models import Document
from django import forms

class Docto_Form(ModelForm):
    class Meta:
        model = Document
        exclude = ['user']

class Docto_Update(ModelForm):
	class Meta:
	    model = Document
	    fields = "__all__"

class Docto_Form_With_Proposal(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('title','docto_pro')

class Docto_Form_With_Agreement(forms.ModelForm):
	class Meta:
	    model = Document
	    fields = "__all__"
        exclude = ['proposal']
