from django.shortcuts import render
from django.views import generic
from .models import Storie


class StorieList(generic.ListView):
    model = Storie
    queryset = Storie.objects.filter(status=1).order_by('posted_on')
    template_name = 'index.html'
    paginate_by = 8

