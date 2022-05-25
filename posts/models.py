from django.db import models
from spaces.models import (
    Space
)
from accounts.models import (
    User
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    video = models.FileField(upload_to="videos", null=True, blank=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    likes = models.ManyToManyField(User, null=True, blank=True, related_name="liked_comments")
    dislikes = models.ManyToManyField(User, null=True, blank=True, related_name="disliked_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
