from django.shortcuts import HttpResponse,render

def index(request):
    return render(request, 'login.html')

def submit(request):
    print(request.headers)
    return HttpResponse('')