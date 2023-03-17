# Generated by Django 4.1.7 on 2023-03-08 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0004_customer_state_alter_customer_zipcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("Pr", "------------"),
                    ("ec", "Eastern Cape"),
                    ("fs", "Free State"),
                    ("gt", "Gauteng"),
                    ("kzn", "KwaZulu-Natal"),
                    ("lp", "Limpopo"),
                    ("mp", "Mpumalanga"),
                    ("nc", "Northern Cape"),
                    ("nw", "North West"),
                    ("wc", "Western Cape"),
                ],
                default="",
                max_length=200,
            ),
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveBigIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]