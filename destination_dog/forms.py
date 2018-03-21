from django import forms
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article
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