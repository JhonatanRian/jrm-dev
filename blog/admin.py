from django.contrib import admin

from blog.models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "published", "published_at", "created_at")
    list_filter = ("published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)
