from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Drafts"), (1, "Published"))


class PostStorie(models.Model):
    """
    the poststorie model what is been used when creating post as a user
    """
    title = models.CharField(max_length=60, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    posted_image = CloudinaryField('image', default='placeholder')
    posted_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    liked_story = models.ManyToManyField(User, related_name="storylike", blank=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.title

    def post_like(self):
        return self.likes.count()
