import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import KeyPapersData, KeyWebsitesData


def returnKeySourcesPage(request):
  papers = KeyPapersData.objects.all()
  websites = KeyWebsitesData.objects.all()
  context = {
    'papers': papers,
    'websites': websites
  }
  return render(request, "keysources/key_sources_page.html", context)

def download_paper(request, path):
  file_path = os.path.join(settings.MEDIA_ROOT, path)
  if os.path.exists(file_path):
    with open(file_path, 'rb') as fh:
      response = HttpResponse(fh.read(), content_type="application/paperFile")
      response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
      return response
  raise Http404