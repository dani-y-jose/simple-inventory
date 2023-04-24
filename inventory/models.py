from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    class Type(models.TextChoices):
        RETAIL = "RE", _("Retail")
        WHOLESALE = "WH", _("Wholesale")
        PARTNER = "PA", _("Partner")

    type = models.CharField(max_length=100, choices=Type.choices, default=Type.RETAIL)
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.full_name


class Region(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# Example of status: Archived, Reserved, Lent, Borrowed, others
class ItemStatus(models.Model):
    item_status = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name_plural = "Item status"

    def __str__(self):
        return self.item_status


class Item(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    item_status = models.ForeignKey(
        ItemStatus, null=True, blank=True, on_delete=models.PROTECT
    )
    active = models.BooleanField()
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order_date = models.DateTimeField("date ordered")
    check_date = models.DateTimeField("date checked")

    def __str__(self):
        return self.model


# class User(models.Model):


class ItemEvent(models.Model):
    class Type(models.TextChoices):
        CHECKIN = "CH", _("Check in")
        STORED = "ST", _("Stored in warehouse")
        BORROWED = "BO", _("Borrowed")
        RETURNED = "RE", _("Returned")
        DAMAGED = "DA", _("Damaged")
        REPAIR = "RP", _("Out for repair")
        LOST = "LO", _("Lost")
        SOLD = "SO", _("Sold")

    type = models.CharField(max_length=100, choices=Type.choices, default=Type.CHECKIN)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestamp = models.DateTimeField("date and time event")
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.PROTECT
    )

    # user_id = models.ForeignKey(
    #    User, null=True, blanck=True, on_delete=models.PROTECT
    # )
    # TODO: add is_lot property
    def __str__(self):
        return self.type
