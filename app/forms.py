from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['topic_name','name','url']
        help_texts={'topic_name':'it will take only topic_name','name':'it will take only names','url':'this take only url form'}
        