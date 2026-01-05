from django.shortcuts import render,redirect, get_object_or_404 # Django uses an ORM layer through which we can interact with the database
from .models import Tweet
from .forms import TweetForm


# Create your views here.

# def index(request):
#     return render(request,'tweet/index.html')


# Method for rendering all the tweets at once in the front page 
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {'tweets':tweets})

# Tweet/Post creation method
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)# Taking the inputs as objects so i can get media files 
        if form.is_valid():
            tweet=form.save(commit=False)# saving the tweet temporarily 
            tweet.user = request.user # when a request comes from a form we get the user from the request not the form
            tweet.save()# permanently saving the tweet in the database 
            return redirect('tweet_list')
    else:
        form = TweetForm()
        
    return render(request, 'tweet_form.html', {'form':form})

# Tweet/Post editing method    
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)# pinpointing which tweet we are editing. and make it so a user can't edit every tweet but his own 
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)# instance is to show what is already in that field  
        
    return render(request, 'tweet_form.html', {'form':form})