from django import forms
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article, Event, Dotw, Service
from datetime import date

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class AddArticleForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Title:")
    author = forms.CharField(max_length=128, help_text="Author:")
    image = forms.ImageField(help_text="Header Image", required=False)
    article = forms.CharField(widget=forms.Textarea, help_text="Article Content")
    date = forms.DateField(widget=forms.HiddenInput(), initial=date.today())

    class Meta:
        model = Article
        fields = (
            'title',
            'author',
            'image',
            'article',
            'date',
        )

class DotwForm(forms.ModelForm):

    dog = forms.CharField(max_length=128, help_text="Dog Name:")
    owner = forms.CharField(max_length=128, help_text="Owner:")
    image = forms.ImageField(help_text="Photo", required=False)

    class Meta:
        model = Dotw
        fields = (
            'dog',
            'owner',
            'image',
        )

class AddEventForm(forms.ModelForm):

    name = forms.CharField(label="Event Name:", max_length=128,)
    description = forms.CharField(widget=forms.Textarea,label="Description:")
    location = forms.CharField(label="Event Location:")
    date = forms.DateField(widget=forms.DateInput(format="%d-%m-%Y"))
    time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"))

    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date', 'time')

class ServiceForm(forms.ModelForm):

    serType = forms.CharField(label="Service Type", max_length=128)
    name = forms.CharField(label="Business Name", max_length=128)
    location = forms.CharField(label="Location", max_length=128)
    daysOpen = forms.CharField(label="Days Open", max_length=128)
    timesOpen = forms.CharField(label="Times Open", max_length=128)
    description = forms.CharField(label="Description", max_length=128)
    ratings = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Service
        fields = ('serType', 'name', 'location', 'daysOpen', 'timesOpen', 'description', 'ratings',)