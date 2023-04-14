from django.contrib import admin
from inventory.models import Item, ItemEvent, Customer, Location

admin.site.register(Item)
admin.site.register(ItemEvent)
admin.site.register(Customer)
admin.site.register(Location)
