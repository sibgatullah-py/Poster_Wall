from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta: # This is a django standerd practice to use the meta class after a form class .
        model = Tweet
        fields = ['title','text','photo'] # fields takes array input so i did array here 
        