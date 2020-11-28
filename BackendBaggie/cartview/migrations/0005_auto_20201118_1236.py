# Generated by Django 3.1.1 on 2020-11-18 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20201117_1701'),
        ('cartview', '0004_auto_20201117_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartveiw',
            name='customerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartveiw',
            name='productID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]
