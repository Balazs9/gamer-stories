from django import forms
from django.forms import ModelForm
from .models import PostStorie


class StorieForm(forms.ModelForm):
    class Meta:
        model = PostStorie
        fields = [
            'title',
            'author',
            'content'
        ]