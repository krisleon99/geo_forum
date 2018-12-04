from django.forms import ModelForm
from .models import Topic, Forum, ForumLike
# from django.forms.util import flatatt


class Topic_Form(ModelForm):
    class Meta:
        model = Topic
        fields = ['title','comment']

class Topic_Update(ModelForm):
    class Meta:
        model = Topic
        fields = ['user','title','comment', 'creation_date', 'is_globally_pinned',]


class Topic_Save(ModelForm):
    class Meta:
        model = Topic
        fields = ['user','title','comment', 'creation_date', 'is_globally_pinned',]

class Forum_Form(ModelForm):
    class Meta:
        model = Forum
        fields = ['comment']

class Forum_Save(ModelForm):
    class Meta:
        model = Forum
        fields = ['user','topic','comment', 'comment_html', 'creation_date',]

class LikeChatForm(ModelForm):
    class Meta:
        model = ForumLike
        fields = '__all__'
