from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django_filters.views import FilterView

from core.views.mixins import AdminPermissionMixin
from portfolio.filters import StackFilter
from portfolio.forms import StackForm
from portfolio.models import Stack


class StackListView(AdminPermissionMixin, FilterView):
    model = Stack
    template_name = "portfolio/admin/stack/stack_list.html"
    context_object_name = "stacks"
    filterset_class = StackFilter
    paginate_by = 10


class StackDetailView(AdminPermissionMixin, DetailView):
    model = Stack
    template_name = "portfolio/admin/stack/stack_detail.html"
    context_object_name = "stack"


class StackCreateView(AdminPermissionMixin, CreateView):
    model = Stack
    form_class = StackForm
    template_name = "portfolio/admin/stack/stack_form.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form):
        messages.success(self.request, "Stack criada com sucesso!")
        return super().form_valid(form)


class StackUpdateView(AdminPermissionMixin, UpdateView):
    model = Stack
    form_class = StackForm
    template_name = "portfolio/admin/stack/stack_form.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form):
        messages.success(self.request, "Stack atualizada com sucesso!")
        return super().form_valid(form)


class StackDeleteView(AdminPermissionMixin, DeleteView):
    model = Stack
    template_name = "portfolio/admin/stack/stack_confirm_delete.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form):
        messages.success(self.request, "Stack excluída com sucesso!")
        return super().form_valid(form)
