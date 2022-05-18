from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PostStorie
from .forms import StorieForm
from django.urls import reverse_lazy
from django.contrib import messages


class StorieCreate(CreateView):
    """
    Create a post as a user
    """
    model = PostStorie
    template_name = 'create_post.html'
    fields = ['title', 'author', 'content', 'posted_image', 'status']
    success_url = reverse_lazy('home')


class PostStorieDetail(DetailView):
    """
    Displaying created stories from the user
    """
    model = PostStorie
    queryset = PostStorie.objects.filter(status=1).order_by('-posted_date')
    template_name = 'post_detail.html'

    def get_comment(self, request, pk, *args, **kwargs):
        queryset = PostStorie.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        usercomments = post.usercomments.filter(approved=True).order_by('-posted_date')

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'usercomments': usercomments,
                'commented': False,
                'comment_form': StorieForm() 
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = PostStorie.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        usercomments = post.usercomments.filter(approved=True).order_by('-posted_date')

        comment_form = StorieForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = StorieForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'usercomments': usercomments,
                'commented': True,
                'comment_form': comment_form
            },
        )


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
