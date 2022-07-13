from django.contrib import admin
from .models import Post, Comment

#Admin page functionality for posts

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish_date')
    list_filter = ('publish_date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body', 'topic']

admin.site.register(Comment)