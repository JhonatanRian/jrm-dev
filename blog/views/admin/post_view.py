from django.contrib import messages
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
    model = Post
    template_name = "blog/admin/post_list.html"
    context_object_name = "posts"
    filterset_class = PostFilter
    paginate_by = 10


class PostDetailView(AdminPermissionMixin, DetailView):
    model = Post
    template_name = "blog/admin/post_detail.html"
    context_object_name = "post"


class PostCreateView(AdminPermissionMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/admin/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post criado como rascunho com sucesso!")
        return super().form_valid(form)


class PostUpdateView(AdminPermissionMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/admin/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        messages.success(self.request, "Post atualizado com sucesso!")
        return super().form_valid(form)


class PostTogglePublishView(AdminPermissionMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post_obj = get_object_or_404(Post, pk=pk)
        if post_obj.published:
            post_obj.published = False
            messages.success(request, f"Post '{post_obj.title}' despublicado com sucesso!")
        else:
            post_obj.published = True
            messages.success(request, f"Post '{post_obj.title}' publicado com sucesso!")
        post_obj.save()
        return redirect("blog:post_list")
