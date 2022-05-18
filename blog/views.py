from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from .models import Storie, Comment
from story.models import PostStorie
from .forms import CommentForm
from django.urls import reverse_lazy


class StorieList(generic.ListView):
    """
    Listing the post what has been created by site admin
    """
    model = Storie
    queryset = Storie.objects.filter(status=1).order_by('-posted_date')
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'post_storie_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['storie'] = Storie.objects.filter(status=1).order_by('-posted_date')
        context['poststorie'] = PostStorie.objects.filter(status=1).order_by('-posted_date')
        return context


class StorieDetail(View):
    """
    Display the individual post page
    """
    def get(self, request, pk, *args, **kwargs):
        queryset = Storie.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('-posted_date')

        return render(
            request,
            "comment_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = Storie.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('-posted_date')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "comment_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form
            },
        )


class StorieLike(View):
    """
    User can like or dislike a post
    """
    def post(self, request, pk):
        post = get_object_or_404(Storie, pk=pk)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('storie_detail', args=[pk]))


class StorieUpdate(UpdateView):
    """
    Update the created post, only admin
    """
    model = Storie
    fields = ['title', 'author', 'content', 'posted_image']
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')


class StorieDelete(DeleteView):
    """
    Delete the post, only admin
    """
    model = Storie
    fields = ['title', 'author', 'content', 'posted_image']
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

