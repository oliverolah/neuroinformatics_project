from django.db import models


class SubmitData(models.Model):
   submitId = models.AutoField(primary_key=True)
   title = models.CharField(max_length=50, verbose_name="Title")
   firstName = models.CharField(max_length=100, verbose_name="First Name")
   lastName = models.CharField(max_length=100, verbose_name="Last Name")
   email = models.EmailField(max_length=50, verbose_name="Email Address")
   description = models.TextField(max_length=255, verbose_name="Description")
   submitFile = models.FileField(upload_to="submitdata/")
   
   class Meta:
      verbose_name="Submit Data"
      verbose_name_plural="Submit Data"
   
   def __str__(self):
      return f"Data Submission - {self.submitId}"
   