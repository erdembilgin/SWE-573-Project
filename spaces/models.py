from django.db import models
from accounts.models import (
    User
)
# Create your models here.
class Tag(models.Model):
    tags = models.CharField(max_length=100, null=True, blank=True)


class Space(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(blank=True, upload_to='banners', null=True)
    tags = models.TextField(null=True, blank=True)
    user = models.ManyToManyField(User, null=True, blank=True)
    

