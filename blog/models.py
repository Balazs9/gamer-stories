from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Drafts"), (1, "Published"))


class PostStories(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posted_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['posted_date']

    def __str__(self):
        return self.title

