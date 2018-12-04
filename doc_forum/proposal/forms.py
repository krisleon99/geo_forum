from django.forms import ModelForm
from .models import Proposal

class ProposalForm(ModelForm):
    class Meta:
        model = Proposal
        fields = "__all__"

class ProposalUpdate(ModelForm):
	class Meta:
	    model = Proposal
	    fields = "__all__"
