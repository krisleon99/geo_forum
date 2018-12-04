from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class User_Basic_Update(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class User_Change_Password(ModelForm):
    class Meta:
        model = User
        fields = ['password']


class MyUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']