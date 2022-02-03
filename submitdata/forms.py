from django import forms
from django.forms import ModelForm
from .models import SubmitData


# Submit Data form for SubmitData model table DB
class SubmitDataForm(forms.ModelForm):
   class Meta:
      model =  SubmitData
      fields = ('title', 'firstName', 'lastName', 'email', 'description', 'submitFile')
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['title'].widget.attrs.update({
         'class': 'w-full rounded-md', 
         'placeholder': 'Your title',
         "required": True
      })
      self.fields['firstName'].widget.attrs.update({
         'class': 'w-full rounded-md', 
         'placeholder': 'Your first name',
         "required": True
      })
      self.fields['lastName'].widget.attrs.update({
         'class': 'w-full rounded-md', 
         'placeholder': 'Your last name',
         "required": True
      })
      self.fields['email'].widget.attrs.update({
         'class': 'w-full rounded-md', 
         'placeholder': 'your@email.com',
         "required": True
      })
      self.fields['description'].widget.attrs.update({
         'class': 'w-full rounded-md resize-none', 
         'rows': '10',
         'cols':'50', 
         'placeholder': 'Write description here...',
         "required": True
      })


   def clean(self):
      cleaned_data = self.cleaned_data
      print('Data instance information: ', cleaned_data)
      return cleaned_data