from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from datetime import datetime, date

class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='articles') #For the top of the article page
    article = models.TextField()
    date = models.DateField(default=date.today)
    author = models.ForeignKey('UserProfile', related_name='article')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Dotm(models.Model):
    dog = models.CharField(max_length=128)
    owner = models.ForeignKey('UserProfile', related_name='dotm')
    image = models.ImageField(upload_to='dotm')
    created_at = models.DateTimeField(default=datetime.now())
    winner = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Dog of The Month Entries'

    def __str__(self):
        return self.dog

class Dog(models.Model):
    gender_choices = (('M','Male'),('F','Female'))
    name = models.CharField(max_length=128)
    picture = models.CharField(upload_to="dogs")
    breed = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=gender_choices)
    about_me = models.textField()  
    owner = models.ForeignKey('UserProfile', related_name="dog", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
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
    user = models.ForeignKey('Userprofile', related_name="event", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    dogs = models.ForeignKey('Dog', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username




