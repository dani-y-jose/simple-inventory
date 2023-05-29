from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Item

# Create your views here.
# def hello(request):
#   return HttpResponse("Hello my love!")


def index(request):
    return render(request, "inventory/index.html")


def list_items(request):
    items = list(Item.objects.values())
    data = {"items": items}
    return JsonResponse(data)


def items(request):
    return render(request, "inventory/items.html")
