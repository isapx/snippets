from django import forms
from .models import Snippet



class AddSnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
