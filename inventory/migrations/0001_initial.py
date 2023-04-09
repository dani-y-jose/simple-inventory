# Generated by Django 4.1.7 on 2023-04-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=200)),
                ("brand", models.CharField(max_length=200)),
                ("quantity", models.IntegerField(default=0)),
                ("description", models.CharField(max_length=200)),
                ("status", models.CharField(max_length=200)),
                ("active", models.BooleanField()),
                ("type", models.CharField(max_length=200)),
                ("category", models.CharField(max_length=200)),
                ("order_date", models.DateTimeField(verbose_name="date ordered")),
                ("check_date", models.DateField(verbose_name="date published")),
            ],
        ),
    ]
