from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import SubmitData
from .forms import SubmitDataForm


def returnSubmitDataPage(request):
   form = SubmitDataForm(request.POST or None, request.FILES or None)
   data = {}
   
   if request.is_ajax():
      if form.is_valid():  # if valid also cleaned
         # form.save()
         data["status"] = {
            "result": "success",
            "message": "Form valid and submitted",
            "code": "valid"
         }
         form.save()
         return JsonResponse(data)
      else:
         data["status"] = {
            "result": "failed",
            "message": "Form invalid",
            "code": "invalid"
         }
         return JsonResponse(data)
      form = SubmitDataForm()
   context = {
      "form": form,
   }
   return render(request, "submitdata/submit_data_page.html", context)