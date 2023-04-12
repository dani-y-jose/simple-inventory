from django.db import models


class Item(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    # location_id = models.ForeignKey("Location", on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    active = models.BooleanField()
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order_date = models.DateTimeField("date ordered")
    check_date = models.DateTimeField("date checked")

    def __str__(self):
        return self.model


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class ItemEvent(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestamp = models.DateTimeField("date and time event")
    type = models.CharField(max_length=100)
    # location_id = models.ForeignKey("Location", on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    customer_id = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.type
