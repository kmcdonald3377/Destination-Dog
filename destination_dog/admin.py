from django.contrib import admin
from destination_dog.models import Article, UserProfile, Dotw

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Dotw)

