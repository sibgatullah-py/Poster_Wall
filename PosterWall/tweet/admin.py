from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')


admin.site.register(Tweet, TweetAdmin)