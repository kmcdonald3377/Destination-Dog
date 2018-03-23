from django import forms
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article, Event, Dotw
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

    name = forms.CharField(label="Event Name:", max_length=128,help_text="Event Name:")
    description = forms.CharField(widget=forms.Textarea, help_text="Event Description:")
    location = forms.CharField(help_text="Event Location:")
    date = forms.DateField(widget=forms.DateInput(format="%"), help_text="Date:(format yyyy-mm-dd)")

    time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"), help_text="Time:(format hh:mm)")

    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date', 'time')

