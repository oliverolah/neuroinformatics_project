from django.shortcuts import render
from django.http import JsonResponse # HttpResponse
from .models import ContactUsData
from .forms import ContactUsDataForm
# from django.core.mail import send_mail
# from django.conf import settings


def returnContactUsPage(request):
  form = ContactUsDataForm(request.POST or None)
  data = {}
  
  if request.is_ajax():
    if form.is_valid():
      title = form.cleaned_data['title']
      firstName = form.cleaned_data['firstName']
      lastName = form.cleaned_data['lastName']
      email = form.cleaned_data['email']
      description = form.cleaned_data['description']
      
      # subject = f'Contact us form new message from: {email}'
      # body = {
      #   'title': form.cleaned_data['title'],
      #   'firstName': form.cleaned_data['firstName'],
      #   'lastName': form.cleaned_data['lastName'],
      #   'email': form.cleaned_data['email'],
      #   'description': form.cleaned_data['description']
      # }
      # message = "\n".join(body.values())
      # email_receiver = [settings.EMAIL_POST_USER]
      # send_mail(subject, message, email, email_receiver, fail_silently = False)
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
