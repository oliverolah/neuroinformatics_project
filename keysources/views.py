from django.shortcuts import render
from django.http import HttpResponse


def returnKeySourcesPage(request):
  return render(request, "keysources/key_sources_page.html")