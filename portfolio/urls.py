from django.urls import path

from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("stacks/", views.StackListView.as_view(), name="stack_list"),
    path("stacks/create/", views.StackCreateView.as_view(), name="stack_create"),
    path("stacks/<int:pk>/", views.StackDetailView.as_view(), name="stack_detail"),
    path(
        "stacks/<int:pk>/update/", views.StackUpdateView.as_view(), name="stack_update"
    ),
    path(
        "stacks/<int:pk>/delete/", views.StackDeleteView.as_view(), name="stack_delete"
    ),
    path("projects/", views.ProjectListView.as_view(), name="project_list"),
    path("projects/create/", views.ProjectCreateView.as_view(), name="project_create"),
    path(
        "projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"
    ),
    path(
        "projects/<int:pk>/update/",
        views.ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "projects/<int:pk>/delete/",
        views.ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    # GroupStack CRUD
    path("group-stacks/", views.GroupStackListView.as_view(), name="group_stack_list"),
    path(
        "group-stacks/create/",
        views.GroupStackCreateView.as_view(),
        name="group_stack_create",
    ),
    path(
        "group-stacks/<int:pk>/update/",
        views.GroupStackUpdateView.as_view(),
        name="group_stack_update",
    ),
    path(
        "group-stacks/<int:pk>/delete/",
        views.GroupStackDeleteView.as_view(),
        name="group_stack_delete",
    ),
    # Configuration Dashboard
    path("configuration/", views.ConfigurationView.as_view(), name="configuration"),
]
