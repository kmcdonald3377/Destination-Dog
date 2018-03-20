from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='articles', blank=True, null=True) #For the top of the article page
    article = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('UserProfile', related_name='article')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user = models.OneToOneField(User)


website = models.URLField(blank=True)
picture = models.ImageField(upload_to='profile_images', blank=True)


def __str__(self):
    return self.user.username
