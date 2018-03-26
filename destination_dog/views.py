from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



from.forms import UserForm, UserProfileForm, AddArticleForm, DotmForm, AddEventForm, ServiceForm, AddDogForm
from.models import Article, Event, Dotm, User, Service, Dog

from datetime import datetime

def home(request):
    context_dict = {'boldmessage': "Dogs everywhere"}
    return render(request, 'destination_dog/home.html', context=context_dict)

def article_list(request):
    context_dict = {}

    article = Article.objects.order_by('-date')
    context_dict['article'] = article

    return render(request, 'destination_dog/article_list.html', context=context_dict)


def show_article(request, article_title_slug):

    context_dict = {}

    try:
        article = Article.objects.get(slug=article_title_slug)

        context_dict['article'] = article

    except Article.DoesNotExist:
        context_dict['article'] = None

    return render(request, 'destination_dog/article.html', context_dict)

@login_required
def add_article(request):

    user = User.objects.get(username=request.user)
    profile = user.userprofile

    form = AddArticleForm()

    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():

                article = form.save(commit=False)
                article.author = profile

                if 'image' in request.FILES:
                    article.image = request.FILES['image']

                article.save()
                return HttpResponseRedirect(reverse('article_list'))

        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'destination_dog/add_article.html', context=context_dict)


def dotm(request):

    context_dict = {}

    try:
        article = Article.objects.get(is_dotm=True)

        context_dict['article'] = article

    except Article.DoesNotExist:
        context_dict['article'] = None

    return render(request, 'destination_dog/dotm.html', context_dict)

@login_required()
def dotm_vote(request):

    month = datetime.now().month
    year = datetime.now().year

    context_dict = {}
    dotm = Dotm.objects.filter(created_at__month=month, created_at__year=year)
    context_dict['dotm'] = dotm

    return render(request, 'destination_dog/dotm_vote.html', context_dict)

@login_required
def vote_dotm(request):
    dotm_id = None
    if request.method == 'GET':
        dotm_id = request.GET['dotmid']
        likes = 0
        if dotm_id:
            dotm = Dotm.objects.get(id=int(dotm_id))
            if dotm:
                likes = dotm.likes + 1
                dotm.likes = likes
                dotm.save()
            return HttpResponse(likes)

@login_required()
def dotm_enter(request):

    user = User.objects.get(username=request.user)
    profile = user.userprofile

    form = DotmForm()

    if request.method == 'POST':
        form = DotmForm(request.POST)
        if form.is_valid():

                dotm = form.save(commit=False)
                dotm.owner = profile

                if 'image' in request.FILES:
                    dotm.image = request.FILES['image']

                dotm.save()
                return HttpResponseRedirect(reverse('dotm_vote'))

        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'destination_dog/dotm_enter.html', context=context_dict)

def dotm_hall_of_fame(request):

    context_dict = {}
    thisyear = Dotm.objects.filter(winner=True, created_at__year=2018)
    lastyear = Dotm.objects.filter(winner=True, created_at__year=2017)

    context_dict['thisyear'] = thisyear
    context_dict['lastyear'] = lastyear

    return render(request, 'destination_dog/dotm_hall_of_fame.html', context=context_dict)

def locateServices(request):
    context_dict = {}
    service = Service.objects
    return render(request, 'destination_dog/locateservice.html', context=context_dict)

def add_service(request):
    form = ServiceForm()

    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=True)
            service.save()
            return locateServices(request)
        else:
            print(form.errors)
    
    context_dict = {'form':form}
    return render(request, 'destination_dog/add_service.html', context=context_dict)

def events(request):
    events_list = Event.objects.order_by('date')
    context_dict = {'events': events_list}
    return render(request, 'destination_dog/events.html', context=context_dict)

@login_required
def add_events(request):
    form = AddEventForm()
    if request.method == 'POST':
        form = AddEventForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return events(request)
        else:
            print(form.errors)
    return render(request, 'destination_dog/add_events.html', {'form': form})


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


def userprofile(request, username):

    context_dict = {}

    try:
        user = User.objects.get(username=username)
        profile = user.userprofile

        context_dict['profile'] = profile

    except Article.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'destination_dog/userprofile.html', context_dict)

def dogprofile(request, dog):
    
    context_dict = {}
       
    try: 
        dogprofile = User.objects.get(username=dog)

        context_dict['dog'] = dogprofile
        
    except Dog.DoesNotExist:
        context_dict['dog'] = None
        
    return render(request, 'destination_dog/dogprofile.html', context_dict)

@login_required
def addDog(request):

    user = User.objects.get(username=request.user)
    profile = user.userprofile

    form = AddDogForm()
    
    if request.method == 'POST':
        form = AddDogForm(request.POST)
        if form.is_valid():

            dog = form.save(commit=False)
            dog.owner = profile

            if 'picture' in request.FILES:
                dog.picture = request.FILES['picture']
               
            dog.save()
            return dogprofile(request)

        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'destination_dog/addDog.html', context=context_dict)

