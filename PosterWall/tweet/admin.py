from django.contrib import admin
from .models import Tweet, CustomUser
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'photo')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(CustomUser)