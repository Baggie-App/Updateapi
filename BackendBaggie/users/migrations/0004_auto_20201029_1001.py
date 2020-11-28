# Generated by Django 3.1.1 on 2020-10-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200930_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='mobile_number',
            new_name='mobileNumber',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='customer', max_length=15),
        ),
    ]
