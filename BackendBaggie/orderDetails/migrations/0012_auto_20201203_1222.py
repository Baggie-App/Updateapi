# Generated by Django 3.1.1 on 2020-12-03 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderDetails', '0011_auto_20201113_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='toalprice',
            new_name='ordertotal',
        ),
    ]
