from django.contrib import admin
from inventory.models import Item, ItemEvent, Customer, Location, Region, ItemStatus

admin.site.register(Item)
admin.site.register(ItemEvent)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Region)
admin.site.register(ItemStatus)
