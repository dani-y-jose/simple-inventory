from django.urls import path

from inventory import views

urlpatterns = [
    # path("", views.hello, name="index"),
    path("", views.index, name="index"),
    path("list_items/", views.list_items, name="list_items"),
    path("items/", views.items, name="items"),
]
