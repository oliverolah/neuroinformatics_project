from django.contrib import admin
from .models import KeyPapersData, KeyWebsitesData

@admin.register(KeyPapersData)
class KeyPapersDataAdmin(admin.ModelAdmin):
  list_display = ('paperTitle',)
  

@admin.register(KeyWebsitesData)
class KeyWebsitesDataAdmin(admin.ModelAdmin):
  list_display = ('websiteName',)
