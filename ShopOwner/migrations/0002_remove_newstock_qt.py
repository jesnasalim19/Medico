# Generated by Django 4.2.4 on 2024-03-29 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopOwner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstock',
            name='qt',
        ),
    ]
