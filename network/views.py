import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import User, Post, Profile




# All
def index(request):

    user = request.user
    #posts = Post.objects.all().order_by("-datetime")

    p = Paginator(Post.objects.all().order_by("-datetime"), 10)
    page = request.GET.get('page')
    posts = p.get_page(page)

    return render(request, "network/index.html", {
        "posts": posts,
        "show_new":True,
    })

@login_required
def like_post(request, post_id):
    liked = False
    p = Post.objects.get(id=post_id)
    user = request.user
    if p in user.user_liked_posts.all(): 
        user.user_liked_posts.remove(p)
        liked=False
    else:
        user.user_liked_posts.add(p)
        liked=True
    likes_qty = p.likes.count()

    return JsonResponse({
        "post_id": post_id,
        "liked": liked,
        "likes_qty": likes_qty,
    })
    #retornar Json Response atualizando se existe ou não like no post
    
def check_updated_post(request, post_id):

    p = Post.objects.get(id=post_id)
    user = request.user
    liked = True
    if p not in user.user_liked_posts.all(): 
        liked=False
    likes_qty = p.likes.count()

    return JsonResponse({
        "liked": liked,
        "likes_qty": likes_qty,
    })

@login_required
def following_page(request):

    user = request.user
    user_profile = user.user_profile.first()
    users_followed = user_profile.following.all()
    p = Paginator(Post.objects.filter(user__in=users_followed).order_by("-datetime"), 10)
    page = request.GET.get("page")
    posts = p.get_page(page)

    return render(request, "network/index.html", {
        "user": user,
        "posts": posts,
        "home": False,
    })


def edit_post(request, post_id, text):
    post = Post.objects.get(id=post_id)
    if post.user.username == request.user.username:
        post.text = text
        post.save()
    else:        
       return JsonResponse({"error": "Profile or user not found"})   

    ok = text
    return HttpResponse(ok)

def load_profile(request, username):
    follows = False
    logged_username = request.user.username
    # loading logged user information
    profile_user = User.objects.get(username=username)
    profile_username = profile_user.username
    profile_user_posts = profile_user.user_posts.all()
    profile_user_profile = profile_user.user_profile.first()
    profile_user_following = profile_user_profile.following.count()
    profiles_following_user_profile = profile_user.followers.all()
    count = 0
    names=""
    if logged_username == username:
        home = True
    else:
        home = False

    for p in profiles_following_user_profile:
        count +=1
        names += "+ "+ p.user.username
        if logged_username == p.user.username:
            follows = True

    followers = count
    
    p = Paginator(profile_user.user_posts.all().order_by("-datetime"),10)
    page = request.GET.get("page")
    posts = p.get_page(page)

    return render(request, "network/index.html", {
        "profile_username": profile_username,
        "posts": posts,
        "profile":True,
        "home": home,
        "followers":followers,
        "following":profile_user_following,
        "follows":follows,
        "names":names,
    })

@login_required
def update_follow_stats(request, username):

    #if()
    #se o usuario logado segue o usuario informado, parar de seguir
    try:
        logged_user = request.user
        logged_user_profile = logged_user.user_profile.first()
        user_to_check = User.objects.get(username=username)
    except Profile.DoesNotExist:
        return JsonResponse({"error": "Profile or user not found"})   
    
    ok = "caiu em lugar nenhum"
    if check_if_follows(request, username):
        #significa que o usuário logado segue o usuário informado, parar de seguir        
        logged_user_profile.following.remove(user_to_check)
        ok = "Cai no true"
    else:
        logged_user_profile.following.add(user_to_check)
        ok = "Cai no false"    
    

    return HttpResponse(ok)
@login_required
def check_if_follows(request, username):

    logged_user = request.user.username
    user = User.objects.get(username=username)
    user_profile = user.user_profile.first()
    profiles_following_user = user.followers.all()

    for p in profiles_following_user:
       
        if logged_user == p.user.username:
            return True
    
    return False

@login_required
def profile_info(request, username):    
    follows = False
    logged_user_username = request.user.username
    visited_user = User.objects.get(username=username)
    visited_user_profile = visited_user.user_profile.first()
    following = visited_user_profile.following.count()
    followers = visited_user.followers.all()
    count = 0
    names=""    
    profiles_following_user = visited_user.followers.all()

    for p in profiles_following_user:
        count +=1
        names += "+ "+ p.user.username
      
        if logged_user_username == p.user.username:
            follows = True

    followers = count
    
    infos = [following,followers]
    return JsonResponse({
        "infos": infos,
        "follows": follows,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken or error creating profile."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):

    if request.method == "POST":
        post_text = request.POST["text"]
        new_post = Post(user=request.user,text=post_text)
        new_post.save()
        return HttpResponseRedirect(reverse("index"))
    

    
