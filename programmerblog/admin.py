''' Imports for blog admin page '''
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Admin page functionality for posts


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    ''' Class for admin site post '''
    list_display = ('title', 'slug', 'publish_date')
    list_filter = ('publish_date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body', 'topic']
    summernote_fields = ('body')


# Display comments on admin site
admin.site.register(Comment)
