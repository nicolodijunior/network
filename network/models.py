from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user_profile")
    following = models.ManyToManyField(User, blank=True, related_name="followers")

    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name="Post User")
    text = models.CharField(max_length=280, verbose_name="Post Text")
    datetime = models.DateTimeField(auto_now_add=True)  
    likes = models.ManyToManyField(User, blank=True, related_name="user_liked_posts", verbose_name="Post Likes")
    
    """
    def serialize(self):
        return {
            "author": self.user.username,
            "text": self.text,
            "datetime": self.datetime.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes,
        }
 """







