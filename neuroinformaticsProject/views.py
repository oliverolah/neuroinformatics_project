from django.shortcuts import render


def err400Handler(request, exception):
  return render(request, 'errs/err400.html', status=400)

def err403Handler(request, exception):
  return render(request, 'errs/err403.html', status=403)

def err404Handler(request, exception):
  return render(request, 'errs/err404.html', status=404)

def err500Handler(request):
  return render(request, 'errs/err500.html', status=500)



# function for trying out the design of the template
# def err404Handler(request):
#   return render(request, 'errs/err404.html')