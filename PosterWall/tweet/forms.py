from django import forms
from .models import Tweet, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

TAILWIND_INPUT_CLASSES = (
    "w-full px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 "
    "focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500"
)


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title','text','photo']
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


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": TAILWIND_INPUT_CLASSES,
            "placeholder": "Enter your email"
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": TAILWIND_INPUT_CLASSES,
                "placeholder": "Choose a username"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Password widgets
        self.fields["password1"].widget = forms.PasswordInput(attrs={
            "class": TAILWIND_INPUT_CLASSES,
            "placeholder": "Enter password"
        })
        self.fields["password2"].widget = forms.PasswordInput(attrs={
            "class": TAILWIND_INPUT_CLASSES,
            "placeholder": "Confirm password"
        })

        # Remove help_texts
        self.fields["username"].help_text = None
        self.fields["email"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write a comment...',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].help_text = None


