import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','destination_dog_project.settings')

django.setup()

from django.contrib.auth.models import User
from destination_dog.models import Article, UserProfile, Service
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
            "date": '2018-03-24',
            "author": profile,
            "slug": "dog-stuff",
        },
        {
            "title": "More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2018-03-24',
            "author": profile,
            "slug": "more-dog-stuff",
        },
        {
            "title": "Even More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2018-03-24',
            "author": profile,
            "slug": "even-more-dog-stuff",
        }
    ]

    for data in articles:

            article = Article()
            article.title = data['title']
            article.image = data['image']
            article.article = data['article']
            article.date = data['date']
            article.author = data['author']
            article.slug = data['slug']
            article.save()

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

        user = User()
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.password = data['password']
        user.is_superuser = True
        user.save()

        profile = UserProfile(
            user=User.objects.get(username=data['username']),
            picture="profile_images/profile.png"
        )
        profile.save()

def populate_services():
    print("Populating services...")

    services = [
        {
            "serType": "Vet",
            "name" : "Vets'R'Us",
            "location" : "Glasgow University",
            "daysOpen" : "Monday, Tuesday, Wednesday",
            "timesOpen" : "9am - 5pm",
            "contact" : "0141 123 4567",
            "email" : "vetsrus@test.com",
            "description" : "Dogs dogs dogs dogs dogs",
            "slug" : "vets'r'us",
        }
    ]

    for service in services:
        s = Service.objects.get_or_create(username = service["serType"], name = service["name"], location = service["location"], 
        daysOpen = service["daysOpen"], timesOpen = service["timesOpen"], contact = service["contact"], 
        email = service["email"], description = service["description"], slug = service["slug"])
        s.save()


    # Start execution here!
if __name__ == '__main__':

    print("Starting Rango population script...")
    populate_users()
    populate_article()
