# Generated by Django 5.1.4 on 2024-12-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetail",
            fields=[
                (
                    "username",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]
