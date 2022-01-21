from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Storie



class StorieList(generic.ListView):
    model = Storie
    queryset = Storie.objects.filter(status=1).order_by('posted_date')
    template_name = 'index.html'
    paginate_by = 4


class StorieDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Storie.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('posted_date')
        
        return render(request, "comment_detail.html", {"post": post, "comments": comments})



   

        
