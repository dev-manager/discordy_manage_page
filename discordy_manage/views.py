from django.shortcuts import HttpResponse, render
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return
        return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'login.html')


def main(request):
    return render(request, 'index.html')