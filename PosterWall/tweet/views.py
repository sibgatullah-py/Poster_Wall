from django.shortcuts import render,redirect, get_object_or_404 # Django uses an ORM layer through which we can interact with the database
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

# def index(request):
#     return render(request,'tweet/index.html')


# Method for rendering all the tweets at once in the front page 
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {'tweets':tweets})

# Tweet/Post creation method
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)# Taking the inputs as objects so i can get media files 
        if form.is_valid():
            tweet=form.save(commit=False)# saving the tweet temporarily 
            tweet.user = request.user # when a request comes from a form we get the user from the request not the form
            tweet.save()# permanently saving the tweet in the database 
            return redirect('tweet_list') # returning back after handling the form 
    else:
        form = TweetForm()
        
    return render(request, 'tweet/tweet_form.html', {'form':form})

# Tweet/Post editing method 
@login_required   
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)# pinpointing which tweet we are editing. and make it so a user can't edit every tweet but his own 
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        ''' redirect() does NOT take a template path.
            It takes a URL name (the same one you use in {% url %}). '''
    else:
        form = TweetForm(instance=tweet)# instance is to show what is already in that field  
        
    return render(request, 'tweet/tweet_form.html', {'form':form})

# Tweet/Post deleting method
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    
    
    return render(request, 'registration/register.html', {'form':form})