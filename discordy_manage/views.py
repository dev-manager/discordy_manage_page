from django.shortcuts import HttpResponse,render

def index(request):
    return HttpResponse('hello')

def submit(request):
    print(request.headers)
    return HttpResponse('')