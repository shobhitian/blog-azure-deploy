# blog/admin.py
from django.contrib import admin
from .models import Category, Post, Comment, News, Keywords

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('post', 'news', 'keywords')

admin.site.register(Keywords, KeywordsAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('categories',)
    search_fields = ('title', 'content')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'content', 'author')
        }),
        ('Categorization', {
            'fields': ('categories',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('categories',)
    search_fields = ('title', 'content')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'content', 'author')
        }),
        ('Categorization', {
            'fields': ('categories',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'user_name')
    search_fields = ('text', 'user_name')

