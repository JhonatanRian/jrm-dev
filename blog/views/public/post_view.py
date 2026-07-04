from django.views.generic import DetailView
from django_filters.views import FilterView

from blog.filters import PublicPostFilter
from blog.models import Post


class BlogListView(FilterView):
    """Public-facing list of published blog posts with tag and search filtering."""

    model = Post
    queryset = (
        Post.objects.filter(published=True)
        .select_related("author")
        .prefetch_related("tags")
        .order_by("-published_at")
    )
    template_name = "blog/public/blog_list.html"
    context_object_name = "posts"
    filterset_class = PublicPostFilter
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass all tags for the filter pill buttons
        from blog.models import Tag

        context["all_tags"] = (
            Tag.objects.filter(posts__published=True).distinct().order_by("name")
        )
        context["active_tag_slug"] = self.request.GET.get("tag", "")
        context["search_query"] = self.request.GET.get("search", "")
        return context


class BlogDetailView(DetailView):
    """Public-facing detail view for a published blog post."""

    model = Post
    template_name = "blog/public/blog_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            Post.objects.filter(published=True)
            .select_related("author")
            .prefetch_related("tags")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        # Related posts: same tags, excluding current post, random sample of 3
        tag_ids = post.tags.values_list("id", flat=True)
        related_qs = (
            Post.objects.filter(published=True, tags__in=tag_ids)
            .exclude(pk=post.pk)
            .select_related("author")
            .prefetch_related("tags")
            .distinct()
            .order_by("?")[:3]
        )
        context["related_posts"] = related_qs
        return context
