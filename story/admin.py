from django.contrib import admin
from .models import PostStorie, CommentStorie
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostStorie)
class StoryAdmin(SummernoteModelAdmin):
    """
    register the poststorie model
    """
    list_display = ('title', 'status', 'posted_date')
    search = ('title', 'content')
    list_filter = ('status', 'posted_date')
    summernote_fields = ('content',)


@admin.register(CommentStorie)
class CommentStoryAdmin(admin.ModelAdmin):
    """
    register the commentstorie model
    """
    list_display = ('name', 'post', 'user_comment', 'posted_date', 'approved')
    search = ('name', 'email', 'user_comment')
    list_filter = ('posted_date', 'approved')
    actions = ['approve_usercomment']

    def approve_usercomment(self, request, queryset):
        queryset.update(approved=True)