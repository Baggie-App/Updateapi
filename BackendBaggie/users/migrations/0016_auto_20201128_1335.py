# Generated by Django 3.1.1 on 2020-11-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20201102_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profileImage',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]