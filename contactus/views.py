from django.shortcuts import render
from django.http import HttpResponse


def returnContactUsPage(request):
  return render(request, "homeroots/home.html")