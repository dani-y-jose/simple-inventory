from django.contrib import admin
from inventory.models import Item, ItemEvent, Customer

admin.site.register(Item)
admin.site.register(ItemEvent)
admin.site.register(Customer)
