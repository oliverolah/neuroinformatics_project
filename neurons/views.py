from django.shortcuts import render


def returnVisualisationPage(request):
  return render(request, "neurons/visualisations_page.html")