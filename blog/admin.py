from django.contrib import admin
from .models import Author, Category, Tag, Post, Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at',)
    list_filter = ('author', 'created_at','tags')
    search_fields = ('title', 'content', 'tags')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('post', 'author', 'created_at')
    search_fields = ('content',)
