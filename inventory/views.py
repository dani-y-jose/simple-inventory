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
    item_list = Item.objects.all()
    context = {"items": item_list}
    print(context)
    return render(request, "inventory/items.html", context=context)


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item": item}
    return render(request, "inventory/item_detail.html", context)
