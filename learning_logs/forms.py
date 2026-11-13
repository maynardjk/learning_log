from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """Form for creating a new topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        