from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from module import *

def login(request):
    auth_ = auth()
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        hash_pwd = auth_.password(pwd)
        login = auth_.authenticate(userid, hash_pwd)
        if login:
            auth_.logined[userid] = True
        elif login != False:
            auth_.logined = False
        if not auth_.logined.get(userid):
            return render(request, 'login.html')
        return render(request, 'index.html')
    elif request.method == 'GET':
        return render(request, 'login.html')


def main(request):
    return render(request, 'index.html')
