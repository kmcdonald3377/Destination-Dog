from django import forms
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article, Event, Dotw, Service
from datetime import date

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

class UserProfileForm(forms.ModelForm):

    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture',)

class AddArticleForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Title:")
    image = forms.ImageField(help_text="Header Image", required=False)
    article = forms.CharField(widget=forms.Textarea, help_text="Article Content")
    date = forms.DateField(widget=forms.HiddenInput(), initial=date.today())

    class Meta:
        model = Article
        fields = (
            'title',
            'image',
            'article',
            'date',
        )

class DotwForm(forms.ModelForm):

    dog = forms.CharField(max_length=128, help_text="Dog Name:")
    image = forms.ImageField(help_text="Photo", required=False)


    class Meta:
        model = Dotw
        fields = (
            'dog',
            'image',
        )

class AddEventForm(forms.ModelForm):

    name = forms.CharField(label="Event Name:", max_length=128,help_text="Event Name:")
    description = forms.CharField(widget=forms.Textarea, help_text="Event Description:")
    location = forms.CharField(help_text="Event Location:")
    date = forms.DateField(widget=forms.DateInput(format="%"), help_text="Date:(format yyyy-mm-dd)")

    time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"), help_text="Time:(format hh:mm)")

    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date', 'time')

class ServiceForm(forms.ModelForm):
    SERVICE_CHOICES=[
        ('1', 'Vets'),
        ('2', 'Groomers'),
        ('3', 'Pet Shop'),
        ('4', 'Dog Walker'),
        ('5', 'Dog Sitter'),
        ('6', 'Other'),
    ]
    DAY_CHOICES=[
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    serType = forms.CharField(label="Service Type", widget = forms.Select(choices=SERVICE_CHOICES),  help_text="Service Type: *")
    name = forms.CharField(label="Business Name", max_length=128, help_text="Business Name: *")
    location = forms.CharField(label="Location", max_length=128, help_text="Location:")
    daysOpen = forms.CharField(label="Days Open", widget=forms.CheckboxSelectMultiple(choices=DAY_CHOICES), help_text="Days Open:")
    timesOpen = forms.CharField(label="Times Open", max_length=128, help_text="Times Open:")
    contact = forms.CharField()
    email = forms.EmailField()
    description = forms.CharField(label="Description", widget=forms.Textarea, help_text="Description:")
    ratings = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Service
        fields = ('serType', 'name', 'location', 'daysOpen', 'timesOpen', 'description', 'ratings',)
