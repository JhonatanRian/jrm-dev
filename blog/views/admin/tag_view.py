from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django_filters.views import FilterView

from blog.filters import TagFilter
from blog.forms import TagForm
from blog.models import Tag
from core.views.mixins import AdminPermissionMixin


class TagListView(AdminPermissionMixin, FilterView):
    model = Tag
    template_name = "blog/admin/tag_list.html"
    context_object_name = "tags"
    filterset_class = TagFilter
    paginate_by = 10


class TagCreateView(AdminPermissionMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = "blog/admin/tag_form.html"
    success_url = reverse_lazy("blog:tag_list")

    def form_valid(self, form):
        messages.success(self.request, "Tag criada com sucesso!")
        return super().form_valid(form)


class TagUpdateView(AdminPermissionMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "blog/admin/tag_form.html"
    success_url = reverse_lazy("blog:tag_list")

    def form_valid(self, form):
        messages.success(self.request, "Tag atualizada com sucesso!")
        return super().form_valid(form)


class TagDeleteView(AdminPermissionMixin, DeleteView):
    model = Tag
    template_name = "blog/admin/tag_confirm_delete.html"
    success_url = reverse_lazy("blog:tag_list")

    def form_valid(self, form):
        messages.success(self.request, "Tag excluída com sucesso!")
        return super().form_valid(form)
