from django.shortcuts import render
from django.http import HttpResponse


def returnSubmitDataPage(request):
   return render(request, "submitdata/submit_data_page.html")