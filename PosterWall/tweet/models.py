from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)# this will kick in when the post will be added
    updated_at = models.DateTimeField(auto_now=True)# this will kick in when the post gets updated 
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:15]}'