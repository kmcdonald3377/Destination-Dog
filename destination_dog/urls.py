from django.conf.urls import url
from destination_dog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about', views.about, name='about'),
    url(r'articles', views.article_list, name='article'),
]