from django.contrib import admin
from .models import Blog, CategoryPost, SocialNetwork
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    readonly_fields = ['view_count']
    search_fields = ['title', 'id', ]

@admin.register(CategoryPost)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(SocialNetwork)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']