from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def hello(request):
#   return HttpResponse("Hello my love!")


def index(request):
    return render(request, "inventory/index.html")
