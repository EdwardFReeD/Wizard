from django.shortcuts import render
from .models import Login
from django.http import HttpResponseRedirect

def login(request):
    return render(request, "./login/login.html")

def create(request):
    if request.method == "POST":
        tom = Login()
        tom.name = request.POST.get("login")
        tom.age = request.POST.get("password")
        tom.save()
    return HttpResponseRedirect("/")

def index(request):
    people = Login.objects.all()
    return render(request, "index.html", {"people": people})