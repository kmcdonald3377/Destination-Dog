from django import forms
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article, Event, Dotm, Service, Dog


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

    class Meta:
        model = Article
        fields = (
            'title',
            'image',
            'article',
        )

class DotmForm(forms.ModelForm):

    dog = forms.CharField(max_length=128, help_text="Dog Name:")
    image = forms.ImageField(help_text="Photo", required=False)


    class Meta:
        model = Dotm
        fields = (
            'dog',
            'image',
        )
        
class AddDogForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name:")
    breed = forms.CharField(max_length=128, help_text="Breed:")
    gender = forms.ChoiceField(widget=forms.RadioSelect(choices=Dog.gender_choices), help_text="Gender (M/F):")
    picture = forms.ImageField(required=False, help_text="Dog Image:")
    about_me = forms.CharField(widget=forms.Textarea, help_text="About me:")
    
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'gender', 'picture', 'about_me')

class AddEventForm(forms.ModelForm):

    name = forms.CharField(label="Event Name:", max_length=128,help_text="Event Name:")
    description = forms.CharField(widget=forms.Textarea, help_text="Event Description:", required=False)
    location = forms.CharField(help_text="Event Location:", required=False)
    date = forms.DateField(widget=forms.DateInput(format="%"), help_text="Date:(format yyyy-mm-dd)")

    time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"), help_text="Time:(format hh:mm)")

    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date', 'time')

class ServiceForm(forms.ModelForm):
    SERVICE_CHOICES=[
        ('Vets', 'Vets'),
        ('Groomers', 'Groomers'),
        ('Pet Shop', 'Pet Shop'),
        ('Dog Walker', 'Dog Walker'),
        ('Dog Sitter', 'Dog Sitter'),
        ('Other', 'Other'),
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
    location = forms.CharField(label="Location", max_length=128, help_text="Location:", required=False)
    daysOpen = forms.CharField(label="Days Open", widget=forms.CheckboxSelectMultiple(choices=DAY_CHOICES), help_text="Days Open:", required=False)
    timesOpen = forms.CharField(label="Times Open", max_length=128, help_text="Times Open:", required=False)
    contact = forms.CharField(label="Contact", max_length=128, help_text="Contact Information:", required=False)
    email = forms.EmailField(label="Email", max_length=128, help_text="Email Address:", required=False)
    description = forms.CharField(label="Description", widget=forms.Textarea, help_text="Description:", required=False)
    ratings = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Service
        fields = ('serType', 'name', 'location', 'daysOpen', 'timesOpen', 'description', 'ratings',)
