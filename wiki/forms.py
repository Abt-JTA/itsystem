from django import forms
from wiki.models import *


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['title', 'content', 'tags']
        widgets = {
        }
