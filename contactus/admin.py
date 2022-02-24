from django.contrib import admin
from .models import ContactUsData


@admin.register(ContactUsData)
class ContactUsDataAdmin(admin.ModelAdmin):
  list_display = ('submitId', 'title', 'firstName', 'lastName')
  search_fields = ('submitId', 'title', 'firstName', 'lastName')
  list_filter = ('submitId', 'title', 'firstName', 'lastName', 'created')
  ordering = ('created',)