from django.conf.urls import url
from destination_dog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'articles', views.article_list, name='article'),
    url(r'dogoftheweek', views.dogofweek, name='dogoftheweek'),   
    url(r'locateservice', views.locateServices, name='locateservice'),
    url(r'forum', views.forum, name='forum'),
    url(r'events/$', views.events, name='events'),
    url(r'events/add_event/$', views.add_events, name='add_events'),
    url(r'about', views.about, name='about'),
    url(r'contactus', views.contactus, name='contactus'),
    url(r'sitemap', views.sitemap, name='sitemap'),

    url(r'^login/$', views.user_login, name='login'),

    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^register/$', views.register, name='register'),

    url(r'userprofile', views.userprofile, name='userprofile'),
    url(r'dogprofile', views.dogprofile, name='dogprofile'),
    
]
