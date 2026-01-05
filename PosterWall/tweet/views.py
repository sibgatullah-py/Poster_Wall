from django.shortcuts import render,redirect, get_object_or_404 # Django uses an ORM layer through which we can interact with the database
from .models import Tweet
from .forms import TweetForm


# Create your views here.

# def index(request):
#     return render(request,'tweet/index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {'tweets':tweets})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)# Taking the inputs as objects so i can get media files 
        if form.is_valid():
            tweet=form.save(commit=False)# saving the tweet temporarely 
            tweet.user = request.user # when a request comes from a form we get the user from the request not the form
            tweet.save()# permanently saving the tweet in the database 
            return redirect('tweet_list')
    else:
        form = TweetForm()
        
    return render(request, 'tweet_form.html', {'form':form})
    