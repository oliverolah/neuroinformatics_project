from django.contrib import admin
from .models import SubmitData


@admin.register(SubmitData)
class SubmitDataAdmin(admin.ModelAdmin):
   list_display = ('submitId', 'title', 'firstName', 'lastName')
   search_fields = ('submitId', 'title', 'firstName', 'lastName')
   list_filter = ('submitId', 'title', 'firstName', 'lastName')