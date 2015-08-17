from django import forms
from wiki.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.text import slugify
import itertools


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'tags']
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_topicform', 'Submit'))
        super(TopicForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(TopicForm, self).save(commit=False)

        if self.instance.slug:
            return super(TopicForm, self).save()

        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not Topic.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        instance.save()
        return instance
