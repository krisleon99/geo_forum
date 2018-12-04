from django.forms import ModelForm

from doc_forum.fmail.models import SendFmail, TokenF

class SendFmail_Form(ModelForm):
    class Meta:
        model = SendFmail
        fields = ['user_owner','topic','status','creation_date']

class SendFmail_User(ModelForm):
    class Meta:
        model = SendFmail
        fields = ['user_owner','user_follow','status','creation_date']

class SendFmail_Dimension(ModelForm):
    class Meta:
        model = SendFmail
        fields = ['user_owner','dimension','status','creation_date']

class SaveFmailHistory(ModelForm):
	class Meta:
	    model = TokenF
	    fields = ['user','send','subject','body','token','comment_html','creation_date','status','is_autorized']


class UpdateFmailHistory(ModelForm):
	class Meta:
	    model = TokenF
	    fields = ['status']
