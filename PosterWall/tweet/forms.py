from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta: # This is a django standerd practice to use the meta class after a form class .
        model = Tweet
        fields = ['title','text','photo'] # fields takes array input so i did array here 
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'w-full text-sm font-medium text-gray-700 mb-2 px-4 py-2 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 2,
                'placeholder': 'What’s happening?'
            }),
            'text': forms.Textarea(attrs={
                'class': 'w-full text-sm font-medium text-gray-700 mb-2 px-4 py-6 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'What’s happening?'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 '
                         'file:rounded-lg file:border-0 file:text-sm file:font-semibold '
                         'file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
        }
        