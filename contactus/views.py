from django.shortcuts import render
from django.http import JsonResponse # HttpResponse
from .models import ContactUsData
from .forms import ContactUsDataForm


def returnContactUsPage(request):
  form = ContactUsDataForm(request.POST or None)
  data = {}
  
  if request.is_ajax():
    if form.is_valid():
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
    
    form = ContactUsDataForm(data)
  context = {
    "form": form
  }
  return render(request, "contactus/contact_us_page.html", context)
