from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
)
from django_filters.views import FilterView

from blog.filters import PostFilter
from blog.forms import PostForm
from blog.models import Post
from core.views.mixins import AdminPermissionMixin


class PostListView(AdminPermissionMixin, FilterView):
    """View to list blog posts in the admin panel with filtering and pagination."""

    model = Post
    queryset = Post.objects.select_related("author").prefetch_related("tags")
    template_name = "blog/admin/post/post_list.html"
    context_object_name = "posts"
    filterset_class = PostFilter
    paginate_by = 10


class PostDetailView(AdminPermissionMixin, DetailView):
    """View to display details of a specific blog post in the admin panel."""

    model = Post
    template_name = "blog/admin/post/post_detail.html"
    context_object_name = "post"


class PostCreateView(AdminPermissionMixin, CreateView):
    """View to create a new blog post."""

    model = Post
    form_class = PostForm
    template_name = "blog/admin/post/post_form.html"
    success_url = reverse_lazy("blog_admin:post_list")

    def form_valid(self, form: PostForm) -> HttpResponse:
        form.instance.author = self.request.user
        messages.success(self.request, "Post criado como rascunho com sucesso!")
        return super().form_valid(form)


class PostUpdateView(AdminPermissionMixin, UpdateView):
    """View to update an existing blog post."""

    model = Post
    form_class = PostForm
    template_name = "blog/admin/post/post_form.html"
    success_url = reverse_lazy("blog_admin:post_list")

    def form_valid(self, form: PostForm) -> HttpResponse:
        messages.success(self.request, "Post atualizado com sucesso!")
        return super().form_valid(form)


class PostTogglePublishView(AdminPermissionMixin, View):
    """View to toggle the published state of a blog post."""

    def post(self, request: HttpRequest, pk: int, *args, **kwargs) -> HttpResponse:
        post_obj = get_object_or_404(Post, pk=pk)
        post_obj.published = not post_obj.published
        post_obj.save()

        status_msg = "publicado" if post_obj.published else "despublicado"
        messages.success(
            request, f"Post '{post_obj.title}' {status_msg} com sucesso!"
        )
        return redirect("blog_admin:post_list")

