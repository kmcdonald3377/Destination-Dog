from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context_dict = {'boldmessage': "Dogs everywhere"}
    return render(request, 'destination_dog/home.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage' : "enjoy yourself!"}
    return render(request, 'destination_dog/about.html', context=context_dict)

def locateServices(request):
    context_dict = {'boldmessage' : "find a service"}
    return render(request, 'destination_dog/locateservice.html', context=context_dict)

def forum(request):
    context_dict = {'boldmessage' : "chat to people"}
    return render(request, 'destination_dog/forum.html', context=context_dict)