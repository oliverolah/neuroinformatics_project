from django import forms
from django.forms import ModelForm
from .models import SubmitData


# Submit Data form for SubmitData model table DB
class SubmitDataForm(forms.ModelForm):
   class Meta:
      model =  SubmitData
      fields = ('title', 'firstName', 'lastName', 'email', 'description', 'submitFile')

   def clean(self):
      cleaned_data = self.cleaned_data
      print('Data instance information: ', cleaned_data)
      return cleaned_data