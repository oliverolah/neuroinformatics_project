from django import forms
from django.forms import ModelForm
from .models import ContactUsData


class ContactUsDataForm(forms.ModelForm):
  
  title = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'w-full rounded-md',
      'placeholder': 'Your title',
      'required': True
    }
  ))
  firstName = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'w-full rounded-md',
      'placeholder': 'Your first name',
      'required': True
    }
  ))
  lastName = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'w-full rounded-md',
      'placeholder': 'Your last name',
      'required': True
    }
  ))
  email = forms.EmailField(widget=forms.EmailInput(
    attrs={
      'class': 'w-full rounded-md',
      'placeholder': 'your@email.com',
      'required': True
    }
  ))
  description = forms.CharField(widget=forms.Textarea(
    attrs={
      'class': 'w-full rounded-md',
      'rows': '10',
      'cols':'50',
      'placeholder': 'Write description here...',
      'required': True
    }
  ))
  class Meta:
    model = ContactUsData
    fields = (
      'title',
      'firstName',
      'lastName',
      'email',
      'description'
    )