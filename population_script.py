import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','destination_dog_project.settings')

django.setup()

from django.contrib.auth.models import User
from destination_dog.models import Article, UserProfile
from django.contrib.auth.hashers import make_password

from datetime import date



def populate_article():

    print("Populating articles...")
    user = User.objects.get(username="kayleighchisholm")
    profile = user.userprofile

    articles = [
        {
            "title": "Dog Stuff",
            "image": "articles/dog.jpg",
            "article":"Article Content",
            "author": profile,
            "slug": "dog-stuff",
        },
        {
            "title": "More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "author": profile,
            "slug": "more-dog-stuff",
        },
        {
            "title": "Even More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "author": profile,
            "slug": "even-more-dog-stuff",
        }
    ]

    for data in articles:

            a = Article()
            a.title = data['title']
            a.image = data['image']
            a.article = data['article']
            a.date = date.today()
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
            "password": make_password("destinationdog"),
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
        u.is_superuser = True
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
