import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','destinationdog.settings')

django.setup()

from django.contrib.auth.models import User
from destination_dog.models import Article, UserProfile
from django.contrib.auth.hashers import make_password

def populate_article():

    print("Populating articles...")
    user = User.objects.get(username="kayleighchisholm")
    profile = user.userprofile

    articles = [
        {
            "title": "Dog Stuff",
            "image": "articles/dog.jpg",
            "article":"Article Content",
            "date":'2018-03-25',
            "author": profile,
            "slug": "dog-stuff",
        },
        {
            "title": "More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2017-03-25',
            "author": profile,
            "slug": "more-dog-stuff",
        },
        {
            "title": "Even More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2018-01-25',
            "author": profile,
            "slug": "even-more-dog-stuff",
        }
    ]

    for data in articles:

            a = Article()
            a.title = data['title']
            a.image = data['image']
            a.article = data['article']
            a.date = data['date']
            a.author = data['author']
            a.slug = data['slug']
            a.save()

def populate_users():
    print("Populating users...")

    users = [
        {
            "username": "kayleighchisholm",
            "first_name": "Kayleigh ",
            "last_name": "Chisholm",
            "password": make_password("desinationdog"),
        },
        {
            "username": "kellymcdonald",
            "first_name": "Kelly",
            "last_name": "McDonald",
            "password": make_password("destinationdog"),
        },
        {
            "username": "stephanieman",
            "first_name": "Stephanie",
            "last_name": "Man",
            "password": make_password("destinationdog"),
        },
    ]

    for data in users:

        u = User.objects.get_or_create(username=data['username'])[0]
        u.first_name = data['first_name']
        u.last_name = data['last_name']
        u.password = data['password']
        u.save()

        profile = UserProfile(
            user=User.objects.get(username=data['username']),
            picture="profile_images/profile.png"
        )
        profile.save()


    # Start execution here!
if __name__ == '__main__':

    print("Starting Rango population script...")
    populate_users()
    populate_article()
