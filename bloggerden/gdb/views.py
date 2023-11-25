from django.shortcuts import render
from gdb.models import game, alt_name, screenshot
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import redirect

# Create your views here.

def index(request):
    data = game.objects.all()
    return render(request,"index.html", {"games": data})

def game_page(requests,arg):
    res = game.objects.filter(id = arg)
    print (res)
    genres =res[0].genre.all()
    alt_names = alt_name.objects.filter(game = arg)
    screenshots = screenshot.objects.filter(game = arg)
    s = res[0].series.all()
    p = res[0].platform.all()
    # genres = Genres.objects.filter(id = arg)
    return render(requests,"game.html",{'res':res, "genres":genres, "alt_names":alt_names, "series": s, "platforms": p, "screenshots": screenshots})

def test(request):
    return render(request,"test.html")