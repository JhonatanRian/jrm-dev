from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from core.models.base_model import BaseModel


class Post(BaseModel):
    title = models.CharField("Título", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, db_index=True, blank=True)
    content = models.TextField("Conteúdo")
    featured_image = models.ImageField(
        "Imagem de Destaque",
        upload_to="blog/posts/",
        blank=True,
        null=True
    )
    published = models.BooleanField("Publicado", default=False)
    published_at = models.DateTimeField("Publicado em", blank=True, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor",
        related_name="blog_posts"
    )

    tags = models.ManyToManyField(
        "blog.Tag",
        blank=True,
        verbose_name="Tags",
        related_name="posts"
    )

    # Postgres tsvector for Full-Text Search
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]
        indexes = [
            GinIndex(fields=["search_vector"], name="blog_post_search_vector_gin")
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Handle publish status and publication timestamp
        if self.published:
            if not self.published_at:
                self.published_at = timezone.now()
        else:
            self.published_at = None

        super().save(*args, **kwargs)

        # Precompute the Search Vector on PostgreSQL
        from django.contrib.postgres.search import SearchVector
        Post.objects.filter(pk=self.pk).update(
            search_vector=SearchVector("title", "content")
        )



