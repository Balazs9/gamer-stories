from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from blog.models import Storie
from .models import PostStorie
from .forms import StorieForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages


class StorieCreate(CreateView):
    model = PostStorie
    paginate_by = 6
    template_name = 'create_post.html'
    fields = ['title', 'author', 'content', 'posted_image']
    success_url = reverse_lazy('home')
