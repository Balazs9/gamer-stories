from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from blog.models import Storie
from .models import PostStorie
from .forms import StorieForm
from django.views.generic.edit import CreateView


class Stories(generic.ListView):
    model = Storie
    template_name = 'index.html'
    paginate_by = 6


class StorieCreate(CreateView):
    model = Storie
    fields = ['title', 'author']
    template_name = 'create_post.html'