from django import forms
from django.forms import ModelForm
from .models import ContactUsData
from django.core.exceptions import ValidationError


class ContactUsDataForm(forms.ModelForm):
  
  title = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'w-full rounded-md',
      'placeholder': 'Your title',
      'required': True,
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


  def clean(self):
    cleaned_data = self.cleaned_data
    print('Data instance information: ', cleaned_data)
    return cleaned_data
  
  def clean_title(self):
    title = self.cleaned_data['title']
    if len(title) < 5:
      message = 'The title should be at least five characters long'
      raise ValidationError(message)
    elif title.isalpha() == False:
      message = 'The title should contain only characters'
      raise ValidationError(message)
    return self.cleaned_data.get('title', '').strip()
  
  def clean_firstName(self):
    firstName = self.cleaned_data['firstName']
    if len(firstName) < 2:
      message = 'The first name should be at least two characters long'
      raise ValidationError(message)
    elif firstName.isalpha() == False:
      message = 'The first name should contain only characters'
      raise ValidationError(message)
    return self.cleaned_data.get('firstName', '').strip()
  
  def clean_lastName(self):
    lastName = self.cleaned_data['lastName']
    if len(lastName) < 2:
      message = 'The first name should be at least two characters long'
      raise ValidationError(message)
    elif lastName.isalpha() == False:
      message = 'The first name should contain only characters'
      raise ValidationError(message)
    return self.cleaned_data.get('lastName', '').strip()
  
  def clean_description(self):
      description = self.cleaned_data['description']
      if len(description) < 5:
        message = 'The description should be at least five characters long'
        raise ValidationError(message)
      return self.cleaned_data.get('description', '').strip()