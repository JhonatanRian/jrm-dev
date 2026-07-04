from django.contrib import messages
from django.http import HttpResponse
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
    """View to list technology stacks in the admin panel with filtering and pagination."""

    model = Stack
    template_name = "portfolio/admin/stack/stack_list.html"
    context_object_name = "stacks"
    filterset_class = StackFilter
    paginate_by = 10


class StackDetailView(AdminPermissionMixin, DetailView):
    """View to display details of a specific stack in the admin panel."""

    model = Stack
    template_name = "portfolio/admin/stack/stack_detail.html"
    context_object_name = "stack"


class StackCreateView(AdminPermissionMixin, CreateView):
    """View to create a new stack."""

    model = Stack
    form_class = StackForm
    template_name = "portfolio/admin/stack/stack_form.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form: StackForm) -> HttpResponse:
        messages.success(self.request, "Stack criada com sucesso!")
        return super().form_valid(form)


class StackUpdateView(AdminPermissionMixin, UpdateView):
    """View to update an existing stack."""

    model = Stack
    form_class = StackForm
    template_name = "portfolio/admin/stack/stack_form.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form: StackForm) -> HttpResponse:
        messages.success(self.request, "Stack atualizada com sucesso!")
        return super().form_valid(form)


class StackDeleteView(AdminPermissionMixin, DeleteView):
    """View to delete a stack."""

    model = Stack
    template_name = "portfolio/admin/stack/stack_confirm_delete.html"
    success_url = reverse_lazy("portfolio:stack_list")

    def form_valid(self, form: StackForm) -> HttpResponse:
        messages.success(self.request, "Stack excluída com sucesso!")
        return super().form_valid(form)
