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
    model = Project
    template_name = "portfolio/admin/project/project_list.html"
    context_object_name = "projects"
    filterset_class = ProjectFilter


class ProjectDetailView(AdminPermissionMixin, DetailView):
    model = Project
    template_name = "portfolio/admin/project/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(AdminPermissionMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolio/admin/project/project_form.html"
    success_url = reverse_lazy("portfolio:project_list")


class ProjectUpdateView(AdminPermissionMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolio/admin/project/project_form.html"
    success_url = reverse_lazy("portfolio:project_list")


class ProjectDeleteView(AdminPermissionMixin, DeleteView):
    model = Project
    template_name = "portfolio/admin/project/project_confirm_delete.html"
    success_url = reverse_lazy("portfolio:project_list")
