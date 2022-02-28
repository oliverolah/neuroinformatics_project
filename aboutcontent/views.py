from django.shortcuts import render
from django.http import HttpResponse


def returnAboutPage(request):
  return render(request, "aboutcontent/about_page.html")