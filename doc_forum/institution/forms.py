from django.forms import ModelForm
from .models import Institution

class Institution_Form(ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"

class Institution_Update(ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
