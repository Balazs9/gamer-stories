from django.contrib import admin
from blog.models import Storie
from .models import PostStorie
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostStorie)
class StoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'posted_date')
    search = ('title', 'content')
    list_filter = ('status', 'posted_date')
    summernote_fields = ('content',)
