from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, "core/index.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "core/tweet_list.html", {"tweets": tweets})


def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

        pass
    else:
        form = TweetForm()
        return render(request, "core/tweet_form.html", {"form": form})


def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
        return render(request, "core/tweet_form.html", {"form": form})


def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    else:
        return render(request, "core/tweet_confirm_delete.html", {"tweet": tweet})

    
