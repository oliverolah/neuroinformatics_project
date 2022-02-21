from django import forms
from django.forms import ModelForm
from .models import SubmitData
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# import re
import os
import magic


# Submit Data form for SubmitData model table DB
class SubmitDataForm(forms.ModelForm):
   
   # def __init__(self, *args, **kwargs):
   #    super(SubmitDataForm, self).__init__(*args, **kwargs)
   #    self.fields['title'].strip = False
   
   class Meta:
      model =  SubmitData
      fields = (
         'title', 
         'firstName', 
         'lastName', 
         'email', 
         'description', 
         'submitFile'
      )

   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['title'].widget.attrs.update({
         'class': 'w-full rounded-md form-control', 
         'placeholder': 'Your title',
         'required': True,
         # 'strip': False,
         # 'trim_whitespace': False,
      })
      self.fields['firstName'].widget.attrs.update({
         'class': 'w-full rounded-md form-control', 
         'placeholder': 'Your first name',
         'required': True
      })
      self.fields['lastName'].widget.attrs.update({
         'class': 'w-full rounded-md form-control', 
         'placeholder': 'Your last name',
         'required': True
      })
      self.fields['email'].widget.attrs.update({
         'class': 'w-full rounded-md form-control', 
         'placeholder': 'your@email.com',
         'required': True
      })
      self.fields['description'].widget.attrs.update({
         'class': 'w-full rounded-md resize-none form-control', 
         'rows': '10',
         'cols':'50', 
         'placeholder': 'Write description here...',
         'required': True
      })


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
   
   # def clean_email(self):
   #    email = self.cleaned_data['email']
   #    reg = r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
   #    if not re.fullmatch(reg, email):
   #       message = 'Invalid email address format'
   #       raise ValidationError(message)
   #    return email
   
   def clean_description(self):
      description = self.cleaned_data['description']
      if len(description) < 5:
         message = 'The description should be at least five characters long'
         raise ValidationError(message)
      return self.cleaned_data.get('description', '').strip()
   
   def clean_submitFile(self):
      submitFile = self.cleaned_data['submitFile']
      max_file_limit = 10 * 1024 *1024
      if submitFile.size > max_file_limit:
         message = 'File size is greater than 10MB. Please, upload the file with a smaller size'
         raise ValidationError(message)
      return submitFile
   
   # CSV format was left out because no magic number was found for it to match its mimetype
   def clean_submitFile(self):
      submitFile = self.cleaned_data['submitFile']
      ext = os.path.splitext(submitFile.name)[1]
      valid_file_extensions = [
         '.pdf', 
         '.docx', 
         '.jpg', 
         '.jpeg', 
         '.png', 
         '.xlsx', 
         '.xls', 
         '.txt',
         '.rar',
         '.zip'
         ]
      if ext.lower() not in valid_file_extensions:
         raise ValidationError('Please upload a file with a valid extension')
      return submitFile 
   
   def clean_submitFile(self):
      submitFile = self.cleaned_data['submitFile']
      valid_mime_types = [
         'application/pdf', 
         'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
         'image/jpeg', 
         'image/png', 
         'jpg', 
         'application/vnd.ms-excel', 
         'application/zip', 
         'application/vnd.rar',
         'text/plain'
      ]
      file_mime_type = magic.from_buffer(submitFile.read(2048), mime=True)
      if file_mime_type not in valid_mime_types:
         raise ValidationError('Invalid file type. Please try again')
      return submitFile
   
   # def clean_strFields(self):
   #    title = self.cleaned_data.get['title']
   #    firstName = self.cleaned_data.get['firstName']
   #    lastName = self.cleaned_data.get['lastName']
   #    email = self.cleaned_data.get['email']
   #    description = self.cleaned_data.get['description']
   #    # submitFile = self.cleaned_data.get['submitFile']
   #    empty_val = ''
   #    str_field = [title, firstName, lastName, email, description]
   #    for field in str_field:
   #       if str_field == empty_val:
   #          message = 'This field is required'
   #          raise ValidationError(message)
   #    return str_field