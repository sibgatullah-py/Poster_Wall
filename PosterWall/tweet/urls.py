from django.urls import path
from . import views
from .views import AboutView


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('my-tweets/',views.my_tweets, name='my_tweets'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),
    path('delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    
    
    path('about/', AboutView.as_view(), name='about'),# this url is for class based views

]

'''
Login, Logout, Password_change, Password_reset 
These methods all comes from the project level url 
path('accounts/', include('django.contrib.auth.urls')),
'''