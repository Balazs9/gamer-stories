from django import forms
from .models import CommentStorie, PostStorie


class StorieForm(forms.ModelForm):
    class Meta:
        model = CommentStorie
        fields = ('user_comment',)
