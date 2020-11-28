from django.db import models

# Create your models here.
#
# class Choice(models.Model):
#     question = models.ForeignKey('Question', on_delete=models.CASCADE)
#     text = models.TextField(null=True, blank=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.text
#
# class Question(models.Model):
#     title = models.TextField(null=False, blank=False)
#     status = models.CharField(default='inactive', max_length=10)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#     @property
#     def choices(self):
#         return self.choice_set.all()

from django.db import models
from os import path
from django.utils.text import slugify
from django.db.models import Lookup, Transform
from django.db.models.fields import Field, CharField


# Create your models here.

# class Image(models.Model):
#     # image = models.CharField(blank=True, null=True, max_length=50)
#     image = models.ImageField(blank=True, null=True, upload_to='')
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=50, unique=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     thumbnail = models.ImageField(blank=True, null=True, upload_to='')
#     images = models.ManyToManyField(Image, related_name='posts')
#
#     def __str__(self):
#         return self.title
#
#     def get_slugged_title(self):
#         return slugify(self.title)

class Task(models.Model):
    title = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(blank=True)
