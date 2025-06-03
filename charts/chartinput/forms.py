from django import forms
from django.forms import ModelForm
from .models import Data, Year

class DataForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'ny meddelelse...'}))

  class Meta:
    model = Data 
    fields = '__all__'

class YearForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'ny meddelelse...'}))

  class Meta:
    model = Year 
    fields = '__all__'