from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Storie
from .models import PostStorie
from .forms import StorieForm
from django.urls import reverse_lazy
from django.contrib import messages


class UserStory(generic.ListView):
    model = PostStorie
    queryset = PostStorie.objects.filter(status=1).order_by('-posted_date')
    template_name = 'user_stories.html'
    paginate_by = 6


class StorieCreate(CreateView):
    """
    Create a post as a user
    """
    model = PostStorie
    template_name = 'create_post.html'
    fields = ['title', 'author', 'content', 'posted_image', 'status']
    success_url = reverse_lazy('user_stories')


class PostStorieDetail(DetailView):
    """
    Displaying created stories from the user
    """
    model = PostStorie
    fields = ['title', 'author', 'content', 'posted_image', 'status']
    template_name = 'post_detail.html'


class UserStorieUpdate(UpdateView):
    """
    Update the created post, when the user logged in
    """
    model = PostStorie
    fields = ['title', 'author', 'content', 'posted_image']
    template_name = 'user_stories_update.html'
    success_url = reverse_lazy('home')


class UserStorieDelete(DeleteView):
    """
    Delete the post, when the user logged in
    """
    model = PostStorie
    fields = ['title', 'author', 'content', 'posted_image']
    template_name = 'user_stories_delete.html'
    success_url = reverse_lazy('home')
