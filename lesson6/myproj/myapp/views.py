from django.shortcuts import render
from myapp.models import Games
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if request.session.get("is_auth", False) == True:
        data = Games.objects.all()
        return render(request,"index.html", {"games": data})
    else:
        return redirect(auth)

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data['user'], password=data['psw'])
        if user:
            request.session["is_auth"] = True
            return redirect(index)
        else:
            return render(request,"auth.html",{'title':'Авторизация'})
    return render(request,"auth.html",{'title':'Авторизация'})

def registration(request):
    if request.method == "POST":
        data = request.POST
        is_user = User.objects.filter(username=data['user'])
        if is_user:
            return HttpResponse(f"Пользователь {data['user']} уже существует.")
        else:
            user = User.objects.create_user(data['user'], " ", data['psw'])
            user.save()
            return HttpResponse(f"Пользователь {user.username} был создан.")
    return render(request,"auth.html",{'title':'Регистрация'})

