
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("posts", views.new_post, name="new_post"),
    path("profile/<str:username>", views.load_profile, name="load_profile"),
    path("profile_info/<str:username>", views.profile_info, name = "profile_info"),
    path("update_follow_stats/<str:username>", views.update_follow_stats, name="update_follow_stats"),
    path("following_page", views.following_page, name="following_page"),
    path("edit_post/<int:post_id>/<str:text>", views.edit_post, name="edit_post"),
    path("like/<int:post_id>", views.like_post, name = "like_post"),

    #path("posts/<str:wposts>", views.load_posts, name="load_posts"),
    #path("profile", views.profile, name="profile"),
]
