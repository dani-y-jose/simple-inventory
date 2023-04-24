# Generated by Django 4.1.7 on 2023-04-24 01:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0020_remove_location_type_alter_itemevent_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="location_id",
            new_name="location",
        ),
        migrations.RenameField(
            model_name="itemevent",
            old_name="customer_id",
            new_name="customer",
        ),
        migrations.RenameField(
            model_name="itemevent",
            old_name="item_id",
            new_name="item",
        ),
        migrations.RenameField(
            model_name="itemevent",
            old_name="location_id",
            new_name="location",
        ),
        migrations.RenameField(
            model_name="location",
            old_name="region_id",
            new_name="region",
        ),
    ]
