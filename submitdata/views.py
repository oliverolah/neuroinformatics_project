from django.shortcuts import render
from django.http import JsonResponse # add later => , HttpResponse
from .models import SubmitData
from .forms import SubmitDataForm
# from django.core.mail import send_mail, BadHeaderError


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
         
         # send form email once submitted / once data valid and cleaned
         # subject = "New submit data form information"
         # body = {
         #    'title': form.cleaned_data['title'],
         #    'firstName': form.cleaned_data['firstName'],
         #    'lastName': form.cleaned_data['lastName'],
         #    'email': form.cleaned_data['email'],
         #    'description': form.cleaned_data['description']
         # }
         # message = "\n".join(body.values())
         # try:
         #    send_mail(subject, message, form.cleaned_data['email'], ['mainusercardiffmet@gmail.com'])
         # except BadHeaderError:
         #    return HttpResponse('Invalid header found.')  
         
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