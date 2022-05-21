from django.db import models

# Create your models here.
class Tag(models.Model):
    tags = models.CharField(max_length=100, null=True, blank=True)


class Space(models.Model):
    title = models.TextField()
    description = models.TextField()
    banner = models.ImageField(blank=True, upload_to='banners', null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    

