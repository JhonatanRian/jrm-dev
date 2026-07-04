from django.urls import path

from blog import views

app_name = "blog_admin"

urlpatterns = [
    # ── Tag CRUD ─────────────────────────────────────────────────────────────
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag_delete"),
    # ── Post CRUD ─────────────────────────────────────────────────────────────
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path(
        "posts/<int:pk>/toggle-publish/",
        views.PostTogglePublishView.as_view(),
        name="post_toggle_publish",
    ),
]
