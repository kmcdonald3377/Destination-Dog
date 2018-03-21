import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'destination_dog_project.settings')

import django
django.setup()
from destination_dog.models import Article, UserProfile

def populate():

    userprofiles = [
        {"user" : "A"},
        {"user" : "B"},
        {"user" : "C"},
        {"user" : "D"},
        {"user" : "E"},
        {"user" : "F"},
        {"user" : "G"},
        {"user" : "H"},
        {"user" : "I"},
        {"user" : "J"},
    ]

    articles = [
        {"title": "How to pick a dog", 
        "date": "21st March", 
        "author": userprofiles}
    ]

    for userprofile, userprofile_data in userprofiles.items():
        p = add_user(userprofile)
    

    for article, article_data in articles.items():
        a = add_article(article)
        for au in article_data["author"]:
            add_user

def add_user(user):
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.save()
    return u


def add_article(title, date, au):
    a = Article.objects.get_or_create(title=title, date=date, author=au)[0]
    a.save()
    return a



