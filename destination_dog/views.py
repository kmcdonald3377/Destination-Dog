from django.http import HttpResponse
from django.shortcuts import render
from destination_dog.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

def home(request):
    context_dict = {'boldmessage': "Dogs everywhere"}
    return render(request, 'destination_dog/home.html', context=context_dict)

def article_list(request):
    return render(request, 'destination_dog/article_list.html')    

def dogofweek(request):
    context_dict = {'boldmessage': "pretty dogs"}
    return render(request, 'destination_dog/dow.html', context=context_dict)

def locateServices(request):
    context_dict = {'boldmessage' : "find a service"}
    return render(request, 'destination_dog/locateservice.html', context=context_dict)

def events(request):
    context_dict = {'boldmessage': "find a dog event"}
    return render(request, 'destination_dog/events.html', context=context_dict)

def add_events(request):
    context_dict = {'boldmessage': "add an event"}
    return render(request, 'destination_dog/add_events.html', context=context_dict)

def forum(request):
    context_dict = {'boldmessage' : "chat to people"}
    return render(request, 'destination_dog/forum.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage' : "enjoy yourself!"}
    return render(request, 'destination_dog/about.html', context=context_dict)

def contactus(request):
    context_dict = {'boldmessage' : "tell us something interesting"}
    return render(request, 'destination_dog/contactus.html', context=context_dict)

def sitemap(request):
    context_dict = {'boldmessage' : "find your way around"}
    return render(request, 'destination_dog/sitemap.html', context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    
    else:
        return render(request, 'destination_dog/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
        
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
        
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'destination_dog/register.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registered': registered})

def userprofile(request):
    return render(request, 'destination_dog/userprofile.html') 

def dogprofile(request):
    return render(request, 'destination_dog/dogprofile.html') 


