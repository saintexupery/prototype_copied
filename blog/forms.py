from django import forms
from django.forms import Textarea
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': Textarea(attrs={'cols': 40, 'rows': 2}),
        }