from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Drafts"), (1, "Published"))


class Storie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    posted_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='bloglike', blank=True)
    
    class Meta:
        ordering = ['posted_date']

    def __str__(self):
        return str(self.title)

    def gamers_like(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Storie, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    textbox = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['posted_date']

    def __str__(self):
        return f"{self.name} commented the following: {self.textbox}"


