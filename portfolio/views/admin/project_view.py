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
from portfolio.filters import ProjectFilter
from portfolio.forms import ProjectForm
from portfolio.models import Project


class ProjectListView(AdminPermissionMixin, FilterView):
    """View to list projects in the admin panel with filtering and pagination."""

    model = Project
    queryset = Project.objects.prefetch_related("stacks")
    template_name = "portfolio/admin/project/project_list.html"
    context_object_name = "projects"
    filterset_class = ProjectFilter
    paginate_by = 10


class ProjectDetailView(AdminPermissionMixin, DetailView):
    """View to display details of a specific project in the admin panel."""

    model = Project
    template_name = "portfolio/admin/project/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(AdminPermissionMixin, CreateView):
    """View to create a new project."""

    model = Project
    form_class = ProjectForm
    template_name = "portfolio/admin/project/project_form.html"
    success_url = reverse_lazy("portfolio:project_list")

    def form_valid(self, form: ProjectForm) -> HttpResponse:
        messages.success(self.request, "Projeto criado com sucesso!")
        return super().form_valid(form)


class ProjectUpdateView(AdminPermissionMixin, UpdateView):
    """View to update an existing project."""

    model = Project
    form_class = ProjectForm
    template_name = "portfolio/admin/project/project_form.html"
    success_url = reverse_lazy("portfolio:project_list")

    def form_valid(self, form: ProjectForm) -> HttpResponse:
        messages.success(self.request, "Projeto atualizado com sucesso!")
        return super().form_valid(form)


class ProjectDeleteView(AdminPermissionMixin, DeleteView):
    """View to delete a project."""

    model = Project
    template_name = "portfolio/admin/project/project_confirm_delete.html"
    success_url = reverse_lazy("portfolio:project_list")

    def form_valid(self, form: ProjectForm) -> HttpResponse:
        messages.success(self.request, "Projeto excluído com sucesso!")
        return super().form_valid(form)

