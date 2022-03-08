from django.db import models

class KeyPapersData(models.Model):
  keySourceId = models.AutoField(primary_key=True)
  paperTitle = models.CharField(max_length=255, verbose_name="Paper Title")
  paperFile = models.FileField(upload_to="keypapers/", verbose_name="Paper File")
  
  class Meta:
    verbose_name="Key Papers"
    verbose_name_plural="Key Papers"


class KeyWebsitesData(models.Model):
  keySourceId = models.AutoField(primary_key=True)
  websiteName = models.CharField(max_length=255, verbose_name="Website Name")
  websiteUrl = models.URLField(max_length=255, verbose_name="Website URL")
  
  class Meta:
    verbose_name="Key Websites"
    verbose_name_plural="Key Websites"