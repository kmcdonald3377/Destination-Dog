from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context_dict = {'boldmessage': "Dogs everywhere"}
    return render(request, 'destination_dog/home.html', context=context_dict)
    
def articles(request):
    context_dict = {'boldmessage': "learn about dogs"}
    return render(request, 'destination_dog/article_list.html', context=context_dict)

def dogofweek(request):
    context_dict = {'boldmessage': "pretty dogs"}
    return render(request, 'destination_dog/dow.html', context=context_dict)

def article_list(request):
    return render(request, 'destination_dog/article_list.html')

def locateServices(request):
    context_dict = {'boldmessage' : "find a service"}
    return render(request, 'destination_dog/locateservice.html', context=context_dict)

def events(request):
    context_dict = {'boldmessage': "find a dog event"}
    return render(request, 'destination_dog/events.html', context=context_dict)

def forum(request):
    context_dict = {'boldmessage' : "chat to people"}
    return render(request, 'destination_dog/forum.html', context=context_dict)

<<<<<<< HEAD
def events(request):
    context_dict = {'boldmessage' : 'Welcome to our events page.  We have a list of exciting events for you and'
                                    ' your dog :)'}
    return render(request, 'destination_dog/events.html', context=context_dict)

def add_events(request):
    context_dict = {'boldmessage': "Please add an upcoming event"}
    return render(request, 'destination_dog/add_events.html', context=context_dict)
=======
def about(request):
    context_dict = {'boldmessage' : "enjoy yourself!"}
    return render(request, 'destination_dog/about.html', context=context_dict)

def contactus(request):
    context_dict = {'boldmessage' : "tell us something interesting"}
    return render(request, 'destination_dog/contactus.html', context=context_dict)

def sitemap(request):
    context_dict = {'boldmessage' : "find your way around"}
    return render(request, 'destination_dog/sitemap.html', context=context_dict)



>>>>>>> 831d44c4a67dcfe7efdd9216b5737716f2d6c0ff
