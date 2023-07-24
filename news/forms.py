from django import forms
from .models import New

class NewForm(forms.ModelForm):
    text=forms.CharField(min_length=20)

    class Meta:
        model = New
        fields = ['title',
                  'text',
                  ]