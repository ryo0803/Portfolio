from django import forms
from django.forms import ModelForm
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 10, 'cols': 100}),
        }
