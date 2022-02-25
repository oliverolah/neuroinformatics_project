from django import forms
from django.forms import ModelForm
from .models import ContactUsData


class ContactUsDataForm(forms.ModelForm):
  
  class Meta:
    model = ContactUsData
    fields = (
      'title',
      'firstName',
      'lastName',
      'email',
      'description'
    )