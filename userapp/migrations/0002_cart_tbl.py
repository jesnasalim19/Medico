# Generated by Django 4.2.4 on 2024-03-29 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShopOwner', '0002_remove_newstock_qt'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.reg_tbl')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopOwner.newstock')),
            ],
        ),
    ]
