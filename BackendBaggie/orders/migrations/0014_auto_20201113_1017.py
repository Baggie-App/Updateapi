# Generated by Django 3.1.1 on 2020-11-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201113_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTrakingNumber',
            field=models.CharField(blank=True, default='7927927404', editable=False, max_length=10, unique=True),
        ),
    ]
