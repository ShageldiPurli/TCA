from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Ulanyjylar(AbstractUser):
    user_type_data = ((1, 'Admin'), (2, 'Ulanyjy'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class SliderPic(models.Model):
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sliders/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class News(models.Model):
    name = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='News_image/', blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Agents(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    url = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='AgentsImages/', blank=True, null=True)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)


# Ygtyarnamalar
class Table(models.Model):
    name = models.CharField(max_length=255)
    table = RichTextField()

    def __str__(self):
        return self.name


# Ygtyyarnama patent spisogy
class PermiTable(models.Model):
    name = models.CharField(max_length=255)
    mintable = RichTextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.phone
