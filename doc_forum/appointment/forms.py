from django.forms import ModelForm
from .models import Event

class Event_Form(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date","user"]

class Event_Update(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date"]
