from django.db import models


class ContactUsData(models.Model):
  submitId = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50, verbose_name="Title")
  firstName = models.CharField(max_length=100, verbose_name='FirstName')
  lastName = models.CharField(max_length=100, verbose_name="Last Name")
  email = models.EmailField(max_length=50, verbose_name="Email Address")
  description = models.TextField(max_length=255, verbose_name="Description")
  created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name="Contact Us Data"
    verbose_name_plural="Contact Us Data"