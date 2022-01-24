from django.contrib import admin
from .models import Storie, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Storie)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'posted_date')
    search = ('title', 'content')
    list_filter = ('status', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'your_comment', 'post', 'posted_date', 'approved')
    list_filter = ('posted_date', 'approved')
    search = ('name', 'email', 'your_comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
