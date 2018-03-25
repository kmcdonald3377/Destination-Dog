from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='articles') #For the top of the article page
    article = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('UserProfile', related_name='article')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Dotw(models.Model):
    dog = models.CharField(max_length=128)
    owner = models.ForeignKey('UserProfile', related_name='dotw')
    image = models.ImageField(upload_to='dotw')
    created_at = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name_plural = 'Dog of The Week Entries'

    def __str__(self):
        return self.dog


class Service(models.Model):
    serType = models.CharField(max_length=128)
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    daysOpen = models.CharField(max_length=128)
    timesOpen = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    ratings = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username




