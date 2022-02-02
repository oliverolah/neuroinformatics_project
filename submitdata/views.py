from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import SubmitData
from .forms import SubmitDataForm


def returnSubmitDataPage(request):
   form = SubmitDataForm(request.POST or None, request.FILES or None)
   data = {}
   
   if request.is_ajax():
      if form.is_valid():  # if valid also cleaned
         form.save()
         data["status"] = "Submitted"
         return JsonResponse(data)
      else:
         data["status"] = "Not submitted!"
         return JsonResponse(data)
   context = {
      "form": form,
   }
   return render(request, "submitdata/submit_data_page.html", context)