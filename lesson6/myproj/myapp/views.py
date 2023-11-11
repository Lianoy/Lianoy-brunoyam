from django.shortcuts import render
from myapp.models import Games

# Create your views here.

def index(request):
    data = Games.objects.all()
    return render(request,"index.html", {"games": data})

def test(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        print(data['user'])
    return render(request,"auth.html")
