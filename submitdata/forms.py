from django import forms
from django.forms import ModelForm
from .models import SubmitData


# Submit Data form for SubmitData model table DB
class SubmitDataForm(ModelForm):
   class Meta:
      model =  SubmitData
      fields = ('title', 'firstName', 'lastName', 'email', 'description', 'submitFile')